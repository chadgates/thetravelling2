# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .models import User

from django import forms
from django.utils.translation import ugettext as _

from captcha.fields import ReCaptchaField


class RegistrationForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': _('Name, Surname')}))
    street1 = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': _('Street and House Number')}))
    street2 = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': _('Street and House Number')}))
    zipcode = forms.CharField(max_length=10,  required=True, widget=forms.TextInput(attrs={'placeholder': _('ZIP Code')}))
    city = forms.CharField(max_length=100,  required=True, widget=forms.TextInput(attrs={'placeholder': _('City Name, State')}))
    country = forms.CharField(max_length=100,  required=False, widget=forms.TextInput(attrs={'placeholder': _('Country')}))
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ['username','name', 'street1', 'street2', 'zipcode', 'city', 'country']

    def signup(self, request, user):
        user.name = self.cleaned_data['name']
        user.street1 = self.cleaned_data['street1']
        user.street2 = self.cleaned_data['street2']
        user.zipcode = self.cleaned_data['zipcode']
        user.city = self.cleaned_data['city']
        user.country = self.cleaned_data['country']
        user.save()

