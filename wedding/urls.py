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
    url(
        regex=r'^rsvps/$',
        view=wedding_views.RsvpList.as_view(),
        name='rsvp-list'
    ),

    # GIFTS
    # *****

    url(
        regex=r'^gift/create/$',
        view=wedding_views.GiftCreate.as_view(),
        name='gift-create',
    ),
    url(
        regex=r'^gift/(?P<pk>[\w\-]+)/$',
        view=wedding_views.GiftDetail.as_view(),
        name='gift-detail',
    ),
    # URL pattern for the UpdateView
    url(
        regex=r'^gift/(?P<pk>[\w\-]+)/update/$',
        view=wedding_views.GiftUpdate.as_view(),
        name='gift-update',
    ),
    # URL pattern for the DeleteView
    url(
        regex=r'^gift/(?P<pk>[\w\-]+)/delete/$',
        view=wedding_views.GiftDelete.as_view(),
        name='gift-delete',
    ),
    # URL pattern for the Listview
    url(
        regex=r'^gift/$',
        view=wedding_views.GiftList.as_view(),
        name='gift-list',
    ),

    # CART-ITEMS
    # **********

    url(
        regex=r'^giftbasket/create/$',
        view=wedding_views.CartItemCreate.as_view(),
        name='cart-create',
    ),
    url(
        regex=r'^giftbasket/(?P<pk>[\w\-]+)/$',
        view=wedding_views.CartItemDetail.as_view(),
        name='cart-detail',
    ),
    # URL pattern for the UpdateView
    url(
        regex=r'^giftbasket/(?P<pk>[\w\-]+)/update/$',
        view=wedding_views.CartItemUpdate.as_view(),
        name='cart-update',
    ),
    # URL pattern for the DeleteView
    url(
        regex=r'^giftbasket/(?P<pk>[\w\-]+)/delete/$',
        view=wedding_views.CartItemDelete.as_view(),
        name='cart-delete',
    ),
    # URL pattern for the Listview
    url(
        regex=r'^giftbasket/$',
        view=wedding_views.CartItemList.as_view(),
        name='cart-list',
    ),

    # CART-ITEMS
    # **********

    url(
        regex=r'^order/create/$',
        view=wedding_views.GiftOrderCreate.as_view(),
        name='order-create',
    ),
    url(
        regex=r'^order/$',
        view=wedding_views.GiftOrderList.as_view(),
        name='order-list',
    ),

]
