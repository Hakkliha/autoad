import django_filters

from .models import SalesStatisticModel


class SalesStatisticFilter(django_filters.FilterSet):

    class Meta:
        model = SalesStatisticModel
        fields = ['end_price']
