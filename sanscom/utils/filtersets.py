#-*- coding: utf-8 -*-
import django_filters

from geoads.filtersets import AdFilterSet
from .widgets import IndifferentNullBooleanSelect


class NicerFilterSet(AdFilterSet):
    def __init__(self, *args, **kwargs):
    	super(NicerFilterSet, self).__init__(*args, **kwargs)
        for name, field in self.filters.iteritems():
            if isinstance(field, django_filters.filters.BooleanFilter):
                field.widget = IndifferentNullBooleanSelect()
            if isinstance(field, django_filters.ChoiceFilter):
                # Add "Any" entry to choice fields.
                field.extra['choices'] = tuple([("", u"Tous types"), ] + list(field.extra['choices']))
