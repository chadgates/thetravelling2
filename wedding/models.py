# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class Rsvp(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    will_attend = models.NullBooleanField(verbose_name=_('Attendance'), null=True, blank=True)
    #will_not_attend = models.NullBooleanField(verbose_name=_('Delines with Regrets'))
    guest2 = models.CharField(verbose_name=_('Name, Surname'), max_length=100, blank=True)
    guest3 = models.CharField(verbose_name=_('Name, Surname'), max_length=100, blank=True)
    guest4 = models.CharField(verbose_name=_('Name, Surname'), max_length=100, blank=True)


    class Meta:
        verbose_name = "RSVP"
        verbose_name_plural = "RSVPs"

    def __str__(self):
        return self.user.get_full_name() + ': ' + self.will_attend

    def get_absolute_url(self):
        return reverse('wedding:rsvp-detail', kwargs={'username': self.user.username})
