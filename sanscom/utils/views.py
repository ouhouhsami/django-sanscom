#-*- coding: utf-8 -*-
from datetime import datetime

from django.core import serializers
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.http import HttpResponseRedirect

from geoads.views import AdDeleteView


class CustomAdDeleteView(AdDeleteView):
    """
    Custom Ad delete view that keep deleted items in json format
    """
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete_date = datetime.now()
        self.object.save()
        serialized_obj = serializers.serialize('json', [self.object, ])
        default_storage.save('deleted/%s-%s.json' % (self.object.id, self.object.slug),
                             ContentFile(serialized_obj))
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
