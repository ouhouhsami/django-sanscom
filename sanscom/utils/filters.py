from .fields import NumericRangeField
from django_filters.filters import Filter


class BaseOpenRangeFilter(Filter):
    """
    Abstract class similar to RangeFilter but allows open ended ranges.
    Inheriting classes must define field_class attribute.
    """

    def filter(self, qs, value):
        if value:
            if value.start:
                qs = qs.filter(**{'%s__gte' % self.name: value.start})
            if value.stop:
                qs = qs.filter(**{'%s__lte' % self.name: value.stop})
        return qs


class OpenRangeNumericFilter(BaseOpenRangeFilter):
    field_class = NumericRangeField
