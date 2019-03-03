from labbyims.models import Product_Unit, Location, Room, Product
import django_filters


class ProductFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Product_Unit
        fields = ['description',]

class LocationFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Location
        fields = ['name',]


class ProductCASFilter(django_filters.FilterSet):
    cas = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Product
        fields = ["cas", "name"]