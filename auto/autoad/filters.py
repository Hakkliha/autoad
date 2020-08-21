import django_filters
from .models import Vehicle


class VehicleFilter(django_filters.FilterSet):

    CHOICES = (
        ('price_ascending', 'Price Ascending'),
        ('price_descending', 'Price Descending'),
        ('date_ascending', 'Date Ascending'),
        ('date_descending', 'Date Descending'),
    )

    ordering = django_filters.ChoiceFilter(
        label='Ordering', choices=CHOICES, method='filter_by_order')

    price = django_filters.RangeFilter(label='Price range')

    vehicle_model_year = django_filters.RangeFilter(label='Vehicle model year')

    mileage_km = django_filters.RangeFilter(label='Mileage')

    class Meta:
        model = Vehicle
        fields = ('brand', 'vehicle_model',)

        '''
		fields = {
			'brand': ['iexact'],  --------['icontains']
			'vehicle_model': ['iexact'],
		}
		'''

    def filter_by_order(self, queryset, name, value):
        if value == 'price_ascending':
            expression = 'price'
        elif value == 'price_descending':
            expression = '-price'
        elif value == 'date_ascending':
            expression = 'creation_datetime'
        else:
            expression = '-creation_datetime'
        return queryset.order_by(expression)
