#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

from sanscom.profiles.views import UserProfileDetailView
from sanscom.profiles.forms import UserProfileCustomForm

from userena import views as userena_views

def profiles_urlpatterns(AdModel, AdSearchModel):
    urlpatterns = patterns('',
        url(r'^accounts/profile/$', RedirectView.as_view(url=reverse_lazy('search'))),
        url(r'^accounts/(?P<slug>(?!signout|signup|signin)[\.\w]+)/$',
            UserProfileDetailView.as_view(ad_model=AdModel,
                                          ad_search_model=AdSearchModel),
            name='userena_profile_detail'),
        url(r'^accounts/(?P<username>[\.\w]+)/edit/$',
            userena_views.profile_edit,
            {'template_name': 'userena/profile_form.html', 'edit_profile_form': UserProfileCustomForm},
            name='userena_profile_edit'),
        url(r'^accounts/', include('userena.urls')))
    return urlpatterns
