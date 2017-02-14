# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .models import User

from django import forms
from django.utils.translation import ugettext as _

from captcha.fields import ReCaptchaField


class RegistrationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(
            label=_('Name'), required=True, widget=forms.TextInput(attrs={'placeholder': _('Name, Surname')}))
        self.fields['street1'] = forms.CharField(
            label=_('Street 1'), max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': _('Street and House Number')}))
        self.fields['street2'] = forms.CharField(
            label=_('Street 2'), max_length=100, required=False, widget=forms.TextInput(attrs={'placeholder': _('Street and House Number')}))
        self.fields['zipcode'] = forms.CharField(
            label=_('ZIP Code'), max_length=10,  required=True, widget=forms.TextInput(attrs={'placeholder': _('ZIP Code')}))
        self.fields['city'] = forms.CharField(
            label=_('City'), max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': _('City Name, State')}))
        self.fields['country'] =  forms.CharField(
            label=_('Country'), max_length=100,  required=False, widget=forms.TextInput(attrs={'placeholder': _('Country')}))
        self.fields['captcha'] = ReCaptchaField()

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

