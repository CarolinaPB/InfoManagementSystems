import django_tables2 as tables
from .models import Product_Unit, Location

class Product_UnitTable(tables.Table):
    class Meta:
        model = Product_Unit
        template_name = 'django_tables2/bootstrap.html'
        
class LocationTable(tables.Table):
	    class Meta:
	        model = Location
	        template_name = 'django_tables2/bootstrap.html'
