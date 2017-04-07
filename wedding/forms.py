# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django import forms
from .models import Rsvp, Gift
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
