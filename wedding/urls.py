# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from wedding import views as wedding_views


urlpatterns = [
    # URL pattern for the RSVP Edit/Create
#    url(
#        regex=r'^rsvp/(?P<pk>[\w\-]+)/$',
#        view=wedding_views.RsvpUpdate.as_view(),
#        name='rsvp-update',
#    ),
    # URL pattern for the RSVP Detail
    url(
        regex=r'^rsvps/(?P<username>[\w\-]+)/$',
        view=wedding_views.RsvpDetail.as_view(),
        name='rsvp-detail',
    ),
    url(
        regex=r'^rsvps/~update/$',
        view=wedding_views.RsvpUpdate.as_view(),
        name='rsvp-update'
    ),
]
