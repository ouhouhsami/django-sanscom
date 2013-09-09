#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from geoads.views import (AdDetailView, AdSearchDeleteView,
                          AdSearchUpdateView, AdCreateView, CompleteView,
                          AdPotentialBuyersView, AdPotentialBuyerContactView)
from geoads.contrib.moderation.views import ModeratedAdUpdateView

from sanscom.utils.views import CustomAdDeleteView
from sanscom.utils.forms import PrettyAdPictureForm, HomeContactForm, CustomAdSearchUpdateForm

def ads_urlpatterns(AdModel, AdSearchModel, AdSearchResultModel, AdForm, AdSearchView):
    urlpatterns = patterns('',
        url(r'^(?P<slug>[-\w]+)$', AdDetailView.as_view(model=AdModel, contact_form=HomeContactForm), name="view"),
        url(r'^search/$', AdSearchView.as_view(model=AdModel), name='search'),
        url(r'^search/(?P<search_id>\d+)/$', AdSearchView.as_view(), name='search'),
        url(r'^delete_search/(?P<pk>\d+)$', AdSearchDeleteView.as_view(model=AdSearchModel), name='delete_search'),
        url(r'^edit_search/(?P<pk>\d+)$', AdSearchUpdateView.as_view(model=AdSearchModel, form_class=CustomAdSearchUpdateForm), name="update_search"),
        url(r'^add/$', AdCreateView.as_view(model=AdModel, form_class=AdForm, ad_picture_form=PrettyAdPictureForm), name='add'),
        url(r'^add/complete/$', CompleteView.as_view(), name='complete'),
        url(r'^(?P<pk>\d+)/edit$', ModeratedAdUpdateView.as_view(model=AdModel, form_class=AdForm, ad_picture_form=PrettyAdPictureForm), name='edit'),
        url(r'^(?P<pk>\d+)/delete$', CustomAdDeleteView.as_view(model=AdModel), name='delete'),
        url(r'^contact_buyers/(?P<pk>\d+)$', AdPotentialBuyersView.as_view(model=AdModel, search_model=AdSearchResultModel), name="contact_buyers"),
        url(r'^contact_buyer/(?P<adsearchresult_id>\d+)$', AdPotentialBuyerContactView.as_view(model_class=AdSearchResultModel), name="contact_buyer"),
    )
    return urlpatterns