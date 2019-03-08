from labbyims.models import Product_Unit, Location, Room, Reserve, User, Product, Department
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

class Prod_ResFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model =  Reserve
        fields = ['description',]

class ProductCASFilter(django_filters.FilterSet):
    cas = django_filters.CharFilter(lookup_expr='iexact')
    class Meta:
        model = Product
        fields = ["cas", "name"]

class UserFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = User
        fields = ['id',]

class DeptFilter(django_filters.FilterSet):
    description = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Department
        fields = ['id',]
