# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from .models import Rsvp, CartItem, GiftOrder, GiftOrderItem, Gift
from django.utils.translation import ugettext as _
from django.core.mail import send_mail
from allauth.account.utils import user_email


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


class GiftOrderForm(forms.ModelForm):

    # TODO: check if this is still required
    def __init__(self, *args, **kwargs):
        if kwargs.get('user'):
            self.user = kwargs.pop('user', None)
        super(GiftOrderForm, self).__init__(*args,**kwargs)

    class Meta:
        model = GiftOrder
        fields = ['voucher_from', 'voucher_greeting', 'voucher_senddirect']

    def send_giftorder_mail(self, total_price, user):
        messagetext = _("Thank you so much for ordering a voucher and helping the couple to make their dream come true!") + "\n\n"
        messagetext += _("The voucher will be issued after payment receipt.") + "\n\n"
        messagetext += _("Please send your payment as follows: ") + "\n\n"
        messagetext += _("Bank") + ": Zürcher Kantonalbank" + "\n"
        messagetext += _("Account") +  ": IBAN CH68 0070 0110 0056 1840 3\n"
        messagetext += _("In favour of") + ": Sibylle Widmer + Marco Zurbriggen\n"
        messagetext += _("Amount") + ": " + total_price.__str__() + "\n\n"

        try:
            send_mail(subject="The Travelling 2 - Voucher Order",
                      message=messagetext,
                      from_email="donotreply@thetravelling2.com",
                      recipient_list=[user_email(user)],
                      )
        except:
            pass

