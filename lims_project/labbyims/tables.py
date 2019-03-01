import django_tables2 as tables
from .models import Product_Unit, Location, Reserve

class Product_UnitTable(tables.Table):
    class Meta:
        model = Product_Unit
        fields = ('description', 'product', 'purity', 'curr_amount', \
                'm_unit', 'location', 'exp_date', 'ret_date', 'del_date',\
                'open_date', 'company', 'cat_num', 'batch', 'in_house_no')

        template_name = 'django_tables2/bootstrap.html'

class ReserveTable(tables.Table):
    class Meta:
        model = Reserve
        prod_res = tables.Column(accessor='product_unit.description')
        fields = ('date_res', 'prod_un')



class Product_Unit_MyTable(tables.Table):
    class Meta:
        model = Product_Unit
        fields = ('description', 'product', 'purity', 'curr_amount', \
                'm_unit', 'location', 'exp_date', 'ret_date',  'batch', \
                 'in_house_no' 'del_date', 'open_date', 'company', 'cat_num')

        template_name = 'django_tables2/bootstrap.html'

class LocationTable(tables.Table):
	    class Meta:
	        model = Location
	        template_name = 'django_tables2/bootstrap.html'


class NotificationColumn(tables.Column):
    attrs = {


        'td': {
            'description': lambda Product_Unit: Product_Unit.description,
            'exp_date': lambda Product_Unit: Product_Unit.exp_date,
            'ret_date': lambda Product_Unit: Product_Unit.ret_date,
       }

    }
    def render(self, product_unit):
        return '{} {}'.format(Product_Unit.description, Product_Unit.exp_date, Product_Unit.ret_date)


class FP_Product_UnitTable(tables.Table):
    #product_table = NotificationColumn()
    #attrs = {'width':'20%'}
    class Meta:
        model = Product_Unit
        fields = ('description', 'exp_date', 'ret_date')
        template_name = 'django_tables2/bootstrap.html'

class Product_Unit_ExpTable(tables.Table):
    class Meta:
        attrs = {'width':'10%'}
        model = Product_Unit
        exclude = ('id', ' is_inactive')
        template_name = 'django_tables2/bootstrap-responsive.html'


class LocationTable(tables.Table):
    class Meta:
        model = Location
        template_name = 'django_tables2/bootstrap.html'
