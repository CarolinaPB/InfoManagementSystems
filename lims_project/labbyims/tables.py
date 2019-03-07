import django_tables2 as tables
from django_tables2 import TemplateColumn
from .models import Product_Unit, Location, Reserve, Watching, User
from django_tables2.utils import A

class Product_UnitTable(tables.Table):
    class Meta:
        model = Product_Unit
        fields = ('description', 'product', 'purity', 'curr_amount', \
                'm_unit', 'location', 'exp_date', 'ret_date', 'del_date',\
                'open_date', 'company', 'cat_num', 'batch', 'in_house_no')

        template_name = 'django_tables2/bootstrap.html'

class FP_ReserveTable(tables.Table):
    class Meta:
        model = Reserve
        fields = ('date_res', 'prod_un', 'amount_res')

class FP_Running_LowTable(tables.Table):
    prod_res = tables.Column(accessor='prod_un.description')
    prod_perc = tables.Column(accessor='prod_un.perc_left',\
                verbose_name = '% left')
    perc_left = tables.Column(accessor = 'prod_un.in_house_no')



class Running_LowTable(tables.Table):
        prod_res = tables.Column(accessor='prod_un.description')
        prod_perc = tables.Column(accessor='prod_un.perc_left', \
                    verbose_name = '% left')
        department = tables.Column(accessor = 'dept', \
                    verbose_name = 'Department')
        location = tables.Column(accessor = 'prod_un.location')
        date_exp = tables.Column(accessor = 'prod_un.exp_date')
        date_ret = tables.Column(accessor = 'prod_un.ret_date')
        perc_left = tables.Column(accessor = 'prod_un.in_house_no')
        class Meta:
            template_name = 'django_tables2/bootstrap.html'

class ReserveTable(tables.Table):
    prod_res = tables.Column(accessor='prod_un.description')
    res = tables.Column(accessor = 'user')
    date = tables.Column(accessor = 'date_res')
    meas_u = tables.Column(accessor = 'prod_un.m_unit')
    res_amount = tables.Column(accessor = 'amount_res')
    prod_curr_amount = tables.Column(accessor='prod_un.curr_amount')
    house_no = tables.Column(accessor='prod_un.in_house_no')
    class Meta:
        template_name = 'django_tables2/bootstrap.html'

class Product_Unit_MyTable(tables.Table):
    class Meta:
        model = Product_Unit
        fields = ('description', 'product', 'purity', 'curr_amount', \
                'm_unit', 'location', 'exp_date', 'ret_date',  'batch', \
                 'in_house_no', 'del_date', 'open_date', 'company', 'cat_num')
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
    class Meta:
        model = Product_Unit
        fields = ('description', 'exp_date', 'ret_date')


class Product_Unit_ExpTable(tables.Table):
    class Meta:
        attrs = {'width':'10%'}
        model = Product_Unit
        exclude = ('id', ' is_inactive')
        template_name = 'django_tables2/bootstrap-responsive.html'

class User_info_table(tables.Table):
    class Meta:
        model= User
        #fields = ('username', 'first_name', 'last_name', 'email')
        template_name = 'django_tables2/bootstrap.html'
