# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
import uuid

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

    @property
    def is_taken(self):
        if self.taken_parts < self.max_parts:
            return False
        else:
            return True

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("wedding:gift-detail", kwargs={'pk': self.pk})

    class Meta:
        verbose_name = "Gift"
        verbose_name_plural = "Gifts"


class GiftOrder(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL)
    voucher_from = models.CharField(verbose_name=_('Voucher is from'), max_length=300)
    voucher_greeting = models.TextField(verbose_name=_('Voucher Greeting'), null=True, blank=True)
    voucher_senddirect = models.BooleanField(verbose_name=_('Send voucher directly'), default=False)


class GiftOrderItem(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gift = models.ForeignKey(Gift)
    giftorder = models.ForeignKey(GiftOrder)
    quantity = models.PositiveIntegerField(verbose_name=_('Item count'))


class Cart(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class CartItem(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL)
    gift = models.ForeignKey(Gift)
    amount = models.PositiveIntegerField(verbose_name=_('Item count'))


