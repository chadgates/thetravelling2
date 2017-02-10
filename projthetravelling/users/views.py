# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, redirect_to_login, PermissionDenied

from .models import User


# Source: http://stackoverflow.com/questions/34676751/can-permissionrequiredmixin-and-loginrequiredmixin-be-combined
class LoggedInPermissionsMixin(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated():
            return redirect_to_login(self.request.get_full_path(),
                                     self.get_login_url(), self.get_redirect_field_name())
        if not self.has_permission():
            # We could also use "return self.handle_no_permission()" here
            raise PermissionDenied(self.get_permission_denied_message())
        return super(LoggedInPermissionsMixin, self).dispatch(request, *args, **kwargs)


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'

    # TODO: Write a test function to see if this person has permission to see other users, else
    # redirect him to the "own" page.

    #def test_func(self):
    #    return self.request.user.username==self.model.username


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name',
              'street1',
              'street2',
              'zipcode',
              'city',
              'country',
              'phone',
              ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoggedInPermissionsMixin, ListView):
    permission_required = 'users.view_list'
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
