# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.shortcuts import render

# Create your views here.
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.edit import ModelFormMixin, ProcessFormView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import DetailView, UpdateView, ListView, CreateView, DeleteView
from .models import Rsvp, Gift, GiftOrder, GiftOrderItem, CartItem, GiftOrderStatus
from .forms import RsvpForm, CartItemForm, GiftOrderForm
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import gettext as _
from django.core.urlresolvers import reverse_lazy
from django.db.models import Sum, F, DecimalField
from django.shortcuts import redirect
from decimal import Decimal

# Source: http://stackoverflow.com/questions/17192737/django-class-based-view-for-both-create-and-update
class CreateUpdateView(SingleObjectTemplateResponseMixin, ModelFormMixin,
        ProcessFormView):

    template_name_suffix = '_form'

    def get_object(self, queryset=None):
        try:
            return super(CreateUpdateView,self).get_object(queryset)
        except AttributeError:
            return None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(CreateUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(CreateUpdateView, self).post(request, *args, **kwargs)


class RsvpUpdate(LoginRequiredMixin, UpdateView):

    model = Rsvp
    context_object_name = 'rsvp'
    slug_field = 'user'
    slug_url_kwarg = 'user'
    #fields = [
    #    'will_attend',
    #    'guest2',
    #    'guest3',
    #    'guest4',
    #]
    form_class = RsvpForm

    def get_object(self, queryset=None):

        # get the existing object or created a new one
        obj, created = Rsvp.objects.get_or_create(user=self.request.user)

        return obj

    def get_success_url(self):
        return reverse('wedding:rsvp-detail',
                       kwargs={'username': self.request.user.username})


class RsvpDetail(LoginRequiredMixin, DetailView):

    model = Rsvp
    context_object_name = 'rsvp'
    form_class = RsvpForm

    def get_object(self):
        try:
            obj = Rsvp.objects.get(user__username=self.kwargs['username'])
        except Rsvp.DoesNotExist:
            obj = None

        return obj


class RsvpList(PermissionRequiredMixin, ListView):
    permission_required = 'wedding.view_list'
    model = Rsvp
    context_object_name = 'rsvp_list'
    form_class = RsvpForm
    #slug_field = 'user'
    #slug_url_kwarg = 'user'


class GiftViewMixin(object):
    model = Gift
    context_object_name = 'gift'

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        form.instance.creator = self.request.user.username
        messages.info(self.request, self.success_msg)
        return super(GiftViewMixin, self).form_valid(form)



class GiftList(ListView):

    context_object_name = 'gifts'

    def get_queryset(self):
        return Gift.objects.all().extra(
                    select = {'cart_quantity': """
                    SELECT SUM(quantity) FROM wedding_cartitem
                    WHERE wedding_cartitem.user_id = %s AND wedding_cartitem.gift_id = wedding_gift.id 
                    GROUP BY wedding_cartitem.gift_id
                    """
                    },
                select_params = (self.request.user.id,)).extra(
                    select={'total_taken': """
                    SELECT SUM(quantity) + wedding_gift.taken_parts FROM wedding_cartitem 
                    WHERE wedding_cartitem.user_id = %s AND wedding_cartitem.gift_id = wedding_gift.id 
                    GROUP BY wedding_cartitem.gift_id
                    """},
                select_params = (self.request.user.id,)).extra(
                    select={'total_available': """
                    SELECT wedding_gift.max_parts - SUM(quantity) - wedding_gift.taken_parts FROM wedding_cartitem 
                    WHERE wedding_cartitem.user_id = %s AND wedding_cartitem.gift_id = wedding_gift.id 
                    GROUP BY wedding_cartitem.gift_id
                    """},
                    select_params=(self.request.user.id,)
                )


class GiftDetail(DetailView):
    model = Gift
    context_object_name = 'gift'


class GiftCreate(GiftViewMixin, CreateView):
    success_msg = _("Created")
    fields = ['name',
              'description',
              'link',
              'price',
              'gift_is_part',
              'max_parts',
              'taken_parts',
              'img']

class GiftUpdate(GiftViewMixin, UpdateView):
    success_msg = _("Saved")
    fields = ['name',
              'description',
              'link',
              'price',
              'gift_is_part',
              'max_parts',
              'taken_parts',
              'img']

class GiftDelete(GiftViewMixin, DeleteView):
    success_msg = _("Deleted")
    success_url = reverse_lazy('wedding:gift-list')



class CartItemList(LoginRequiredMixin, ListView):
    #model = CartItem
    context_object_name = 'cartitems'


    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(CartItemList, self).get_context_data(**kwargs)
        context['carttotal'] = CartItem.objects.filter(user=self.request.user).aggregate(total_price=Sum(F('quantity') * F('gift__price'), output_field=DecimalField()))['total_price']


        return context

class CartItemDetail(LoginRequiredMixin, DetailView):
    model = CartItem
    context_object_name = 'cartitem'


class CartItemCreate(LoginRequiredMixin, GiftViewMixin, CreateView):
    success_msg = _("Added to Giftbasket")
    success_url = reverse_lazy('wedding:cart-list')
    form_class = CartItemForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CartItemCreate, self).form_valid(form)

    def form_invalid(self, form):
        response = super(CartItemCreate, self).form_invalid(form)
        return response

class CartItemUpdate(LoginRequiredMixin, GiftViewMixin, UpdateView):
    success_msg = _("Saved")
    fields = ['quantity',
              ]

class CartItemDelete(LoginRequiredMixin, GiftViewMixin, DeleteView):
    model = CartItem
    success_msg = _("Deleted")
    success_url = reverse_lazy('wedding:cart-list')
    context_object_name = 'cartitem'


class GiftOrderCreate(LoginRequiredMixin, GiftViewMixin, CreateView):
    success_msg = _("Successfully sent a gift basket")
    success_url = reverse_lazy('wedding:order-list')
    form_class = GiftOrderForm

    def get_form_kwargs(self):
        kwargs = super(GiftOrderCreate, self).get_form_kwargs()  # put your view name in the super
        user = self.request.user

        if user:
            kwargs['user'] = user

        return kwargs

    def form_valid(self, form):
        new_giftorder = form.save(commit=False)
        calc_total = Decimal('0.00')

        mycart = CartItem.objects.filter(user=self.request.user)

        for item in mycart:
            calc_total = calc_total + (item.quantity * item.gift.price)

        new_giftorder.total_price = calc_total
        new_giftorder.user = self.request.user

        new_giftorder.save()
        form.save_m2m()

        for item in mycart:
            newitem = GiftOrderItem(gift=item.gift, quantity=item.quantity, giftorder=new_giftorder, price=item.gift.price)
            newitem.save()
            gift = Gift.objects.get(id=item.gift.id)
            gift.taken_parts += item.quantity
            gift.save()
            item.delete()

        form.send_giftorder_mail(total_price=calc_total, user=self.request.user)
        return super(GiftOrderCreate, self).form_valid(form)


class GiftOrderList(LoginRequiredMixin, ListView):

    context_object_name = 'giftorders'

    def get_queryset(self):
        return GiftOrder.objects.filter(user=self.request.user)


class OrderStatusList(PermissionRequiredMixin, ListView):
    permission_required = 'wedding.view_list'
    context_object_name = 'giftorders'
    model = GiftOrderStatus


    def get_queryset(self):
        # Fetch the queryset from the parent get_queryset
        queryset = super(OrderStatusList, self).get_queryset()
        sel_payment = self.request.GET.get("sel1")
        sel_voucher = self.request.GET.get("sel2")
        sel_direct = self.request.GET.get("sel3")

        if sel_payment in ('received', 'open'):
            sel_payment = (sel_payment == 'received')
            queryset = queryset.filter(payment_received = sel_payment)

        if sel_voucher in ('issued', 'pending'):
            sel_voucher = ( sel_voucher == 'issued')
            queryset = queryset.filter(voucher_issued = sel_voucher)

        if sel_direct in ('send direct', 'send to user'):
            sel_direct = (sel_direct == 'send direct')
            queryset = queryset.filter(voucher_senddirect = sel_direct)

        return queryset.order_by('-created')


class OrderStatusDetail(PermissionRequiredMixin, DetailView):
    permission_required = 'wedding.view_list'
    context_object_name = 'giftorder'
    model = GiftOrderStatus


class OrderStatusUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'wedding.view_list'
    model = GiftOrderStatus
    context_object_name = 'giftorder'
    success_msg = _("Saved")
    fields = ['payment_received',
              'voucher_issued']
