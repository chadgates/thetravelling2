# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.shortcuts import render

# Create your views here.
from django.views.generic.detail import SingleObjectTemplateResponseMixin
from django.views.generic.edit import ModelFormMixin, ProcessFormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView
from .models import Rsvp
from .forms import RsvpForm
from django.core.urlresolvers import reverse

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
      return Rsvp.objects.get(user__username=self.kwargs['username'])
