# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


@python_2_unicode_compatible
class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    street1 = models.CharField(_('Street 1'), blank=True, max_length=100)
    street2 = models.CharField(_('Street 2'), blank=True, max_length=100)
    zipcode = models.CharField(_('ZIP Code'), blank=True, max_length=10)
    city    = models.CharField(_('City'), blank=True, max_length=100)
    country = models.CharField(_('Country'), blank=True, max_length=100)
    phone   = models.CharField(_('Phone'), blank=True, max_length=100)

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})

    class Meta:
        permissions = (
            ("view_list", "Can see the user list"),
        )
