# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from .models import User

from django import forms
from django.utils.translation import ugettext as _


class RegistrationForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': _('Name, Surname')}))


    class Meta:
        model = User
        fields = ['username','name']

    def signup(self, request, user):
        user.name = self.cleaned_data['name']
        user.save()

