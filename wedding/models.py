# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
import uuid
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit, ResizeCanvas, ResizeToFill
from django.core.mail import send_mail
from allauth.account.utils import user_email
from decimal import Decimal

class TimeStampedModel(models.Model):
    # Abstract base class model that provides self-updating created and modified fields
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Rsvp(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    will_attend = models.NullBooleanField(verbose_name=_('Attendance'), null=True, blank=True)
    guest2 = models.CharField(verbose_name=_('Name, Surname'), max_length=100, blank=True)
    guest3 = models.CharField(verbose_name=_('Name, Surname'), max_length=100, blank=True)
    guest4 = models.CharField(verbose_name=_('Name, Surname'), max_length=100, blank=True)

    def __str__(self):
        return self.user.name + ': ' + ("is coming" if self.will_attend else "not coming")

    def get_absolute_url(self):
        return reverse('wedding:rsvp-detail', kwargs={'username': self.user.username})

    class Meta:
        verbose_name = "RSVP"
        verbose_name_plural = "RSVPs"
        permissions = (
            ("view_list", "Can see the RSVP list"),
        )


class Gift(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name=_('Name'), max_length=300)
    description = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    link = models.TextField(verbose_name=_('Link'), null=True, blank=True)
    price = models.DecimalField(verbose_name=_('Price'), max_digits=7, decimal_places=2)
    gift_is_part = models.BooleanField(verbose_name=_('Gift is part'), default=False)
    max_parts = models.PositiveIntegerField(verbose_name=_('Maximum number of parts'))
    taken_parts = models.PositiveIntegerField(verbose_name=_('Number of parts taken'), default=0)
    img = models.ImageField(blank=True, null=True)
    img_catalog = ImageSpecField(source='img', processors=[ResizeToFit(800, 600), ResizeCanvas(800,600)],
                                 format='JPEG', options={'quality': 60})
    img_miniature = ImageSpecField(source='img', processors=[ResizeToFill(60, 60)],
                                 format='JPEG', options={'quality': 60})

    def is_available(self):
        if self.taken_parts < self.max_parts:
            return True
        else:
            return False

    def avail_parts(self):
        return self.max_parts - self.taken_parts

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wedding:gift-detail", kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Gift"
        verbose_name_plural = "Gifts"
        permissions = (
            ("edit", "Can edit the Gift list"),
        )


class GiftOrder(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    voucher_from = models.CharField(verbose_name=_('Voucher is from'), max_length=300)
    voucher_greeting = models.TextField(verbose_name=_('Voucher Greeting'), null=True, blank=True)
    voucher_senddirect = models.BooleanField(verbose_name=_('Send voucher directly'), default=False)
    payment_received = models.BooleanField(verbose_name=_('Payment received'), default=False)
    voucher_issued = models.BooleanField(verbose_name=_('Voucher issued'), default=False)
    total_price = models.DecimalField(verbose_name=_('Total price'), max_digits=10, decimal_places=2, default=0.00)


    def save(self, *args, **kwargs):
        calc_total = Decimal('0.00')
        mycart = CartItem.objects.filter(user=self.user)
        for item in mycart:
            calc_total = calc_total + (item.quantity * item.gift.price)

        self.total_price = calc_total

        super(GiftOrder, self).save(*args, **kwargs)

        for item in mycart:
            newitem = GiftOrderItem(gift=item.gift, quantity=item.quantity, giftorder=self, price=item.gift.price)
            newitem.save()
            gift = Gift.objects.get(id=item.gift.id)
            gift.taken_parts += item.quantity
            gift.save()
            item.delete()

        messagetext = _("Thank you so much for ordering a voucher and helping the couple to make their dream come true!") + "\n\n"
        messagetext += _("The voucher will be issued after payment receipt.") + "\n\n"
        messagetext += _("Please send your payment as follows: ") + "\n\n"
        messagetext += _("Bank") + ": Zürcher Kantonalbank" + "\n"
        messagetext += _("Account") +  ": IBAN CH68 0070 0110 0056 1840 3\n"
        messagetext += _("In favour of") + ": Sibylle Widmer + Marco Zurbriggen\n"
        messagetext += _("Amount") + ": " + self.total_price.__str__() + "\n\n"

        try:
            send_mail(subject="The Travelling 2 - Voucher Order",
                      message=messagetext,
                      from_email="donotreply@thetravelling2.com",
                      recipient_list=[user_email(self.user)],
                      )
        except:
            pass

    def __str__(self):
        return self.id.__str__() + ": " + self.user.name


class GiftOrderItem(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gift = models.ForeignKey(Gift)
    giftorder = models.ForeignKey(GiftOrder)
    quantity = models.PositiveIntegerField(verbose_name=_('Item count'))
    price = models.DecimalField(verbose_name=_('Price'), max_digits=7, decimal_places=2, default=0.00)

    @property
    def price_total(self):
        return self.quantity * self.price

    def __str__(self):
        return self.gift.name


class Cart(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class CartItem(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    gift = models.ForeignKey(Gift)
    quantity = models.PositiveIntegerField(verbose_name=_('Item count'))


    def get_absolute_url(self):
        return reverse("wedding:cart-detail", kwargs={'pk': self.pk})

    @property
    def price_total(self):
        return self.quantity * self.gift.price

    def __str__(self):
        return self.gift.name + " " + self.id.__str__()
