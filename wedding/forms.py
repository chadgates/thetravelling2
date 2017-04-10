# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from .models import Rsvp, CartItem, GiftOrder
from django.utils.translation import ugettext as _


def get_choices():
    choices = (
        (False, _('Declines with Regrets')),
        (True, _('Accepts with Pleasure. I will be accompanied by:')),
    )

    return choices


class RsvpForm(forms.ModelForm):

    # Source: http://www.ilian.io/django-forms-choicefield-with-dynamic-values/
    def __init__(self, *args, **kwargs):
        super(RsvpForm, self).__init__(*args, **kwargs)
        self.fields['will_attend'] = forms.TypedChoiceField(
            label=_('Attendance'), choices=get_choices(), widget=forms.RadioSelect)

    # will_attend = forms.TypedChoiceField(label=_('Attendance'), choices=choices, widget=forms.RadioSelect)

    class Meta:
        model = Rsvp
        fields = (
            'will_attend',
            'guest2',
            'guest3',
            'guest4',
        )


class CartItemForm(forms.ModelForm):

    class Meta:
            model = CartItem
            fields = ['quantity', 'gift']

    #def __init__(self, *args, **kwargs):
    #    self.user = kwargs.pop('user')
    #    super(CartItemForm, self).__init__(*args, **kwargs)
    #    #self.fields['user'] = self.user


class GiftOrderForm(forms.ModelForm):

    class Meta:
            model = GiftOrder
            fields = ['voucher_from', 'voucher_greeting', 'voucher_senddirect']

