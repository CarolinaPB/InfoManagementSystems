import django_tables2 as tables
from django_tables2 import TemplateColumn
from .models import Product_Unit, Location, Reserve, Watching, Product, \
                    Association
from django_tables2.utils import A

class Product_UnitTable(tables.Table):
    desc = tables.Column(accessor='description')
    prod = tables.Column(accessor='product')
    cas_no = tables.Column(accessor = 'product.cas', verbose_name='CAS')
    house_id = tables.Column(accessor='in_house_no', verbose_name='ID')
    curr_am = tables.Column(accessor='curr_amount', verbose_name='Amount')
    meas_u = tables.Column(accessor='m_unit')
    pur_perc = tables.Column(accessor='purity')
    Loc = tables.Column(accessor='location')
    room = tables.Column(accessor='location.room')
    exp = tables.Column(accessor='exp_date', verbose_name='Expires')
    ret = tables.Column(accessor='ret_date', verbose_name='Retest')
    open = tables.Column(accessor='open_date', verbose_name='Opened')
    deliv = tables.Column(accessor='del_date', verbose_name='Delivered')
    cat_no = tables.Column(accessor='cat_num', verbose_name='Catalog #')
    company = tables.Column(accessor='company')
    batch_no = tables.Column(accessor='batch', verbose_name='Batch #')
    class Meta:
        template_name = 'django_tables2/bootstrap.html'


class FP_ReserveTable(tables.Table):
    ih_id = tables.Column(accessor = 'prod_un.in_house_no', verbose_name = 'ID')
    res =  tables.Column(accessor= 'date_res', verbose_name = 'Date')
    desc = tables. Column (accessor = 'prod_un')
    amount_res = tables.Column(accessor = 'amount_res', verbose_name = 'Amount')



class FP_Running_LowTable(tables.Table):
    perc_lhouse = tables.Column(accessor = 'prod_un.in_house_no', verbose_name='ID')
    prod_res = tables.Column(accessor='prod_un.description', verbose_name='Description')
    prod_perc = tables.Column(accessor='prod_un.perc_left',\
                verbose_name = '% Left', orderable=False)
    exp = tables.Column(accessor = 'prod_un.exp_date', verbose_name = 'Expires')


class Running_LowTable(tables.Table):
        prod_res = tables.Column(accessor='prod_un.description')
        prod_perc = tables.Column(accessor='prod_un.perc_left', \
                    verbose_name = '% Left', orderable=False)
        department = tables.Column(accessor = 'dept', \
                    verbose_name = 'Department')
        location = tables.Column(accessor = 'prod_un.location')
        room = tables.Column(accessor = 'prod_un.location.room')
        date_exp = tables.Column(accessor = 'prod_un.exp_date', verbose_name = 'Expires')
        date_ret = tables.Column(accessor = 'prod_un.ret_date', verbose_name = 'Retest')
        perc_left = tables.Column(accessor = 'prod_un.in_house_no', verbose_name = 'ID')
        comp = tables.Column(accessor = 'prod_un.company')
        cat_no = tables.Column(accessor = 'prod_un.cat_num', verbose_name = 'Catalog #')
        batch = tables.Column(accessor = 'prod_un.batch', verbose_name = 'Batch #')
        class Meta:
            template_name = 'django_tables2/bootstrap.html'


class ReserveTable(tables.Table):
    res_name = tables.Column(accessor = 'res_name')
    prod_res = tables.Column(accessor='prod_un.description')
    date = tables.Column(accessor = 'date_res')
    meas_u = tables.Column(accessor = 'prod_un.m_unit')
    res_amount = tables.Column(accessor = 'amount_res', verbose_name = 'Reserved Amount')
    prod_curr_amount = tables.Column(accessor='prod_un.curr_amount')
    house_no = tables.Column(accessor='prod_un.in_house_no', verbose_name = 'ID')
    prod_loc = tables.Column(accessor='prod_un.location')
    prod_room = tables.Column(accessor='prod_un.location.room', verbose_name='Room')
    class Meta:
        template_name = 'django_tables2/bootstrap.html'


class Product_Unit_MyTable(tables.Table):
    house_id = tables.Column(accessor='prod_un.in_house_no', verbose_name='ID')
    desc = tables.Column(accessor='prod_un.description')
    prod = tables.Column(accessor='prod_un.product')
    batch_no = tables.Column(accessor='prod_un.batch', verbose_name='Batch #')
    curr_am = tables.Column(accessor='prod_un.curr_amount', verbose_name='Amount')
    meas_u = tables.Column(accessor='prod_un.m_unit')
    Loc = tables.Column(accessor='prod_un.location')
    room = tables.Column(accessor='prod_un.location.room')
    exp = tables.Column(accessor='prod_un.exp_date', verbose_name='Expires')
    ret = tables.Column(accessor='prod_un.ret_date', verbose_name='Retest')
    open = tables.Column(accessor='prod_un.open_date', verbose_name='Opened')
    company = tables.Column(accessor='prod_un.company')
    cat_no = tables.Column(accessor='prod_un.cat_num', verbose_name='Catalog #')
    pur_perc = tables.Column(accessor='prod_un.purity')
    class Meta:
        template_name = 'django_tables2/bootstrap.html'


class Product_Unit_ArchTable(tables.Table):
    house_id = tables.Column(accessor='in_house_no', verbose_name='ID')
    desc = tables.Column(accessor='description')
    prod = tables.Column(accessor='product')
    batch_no = tables.Column(accessor='batch', verbose_name='Batch #')
    curr_am = tables.Column(accessor='curr_amount', verbose_name='Amount')
    meas_u = tables.Column(accessor='m_unit')
    Loc = tables.Column(accessor='location')
    room = tables.Column(accessor='location.room')
    exp = tables.Column(accessor='exp_date', verbose_name='Expires')
    ret = tables.Column(accessor='ret_date', verbose_name='Retest')
    open = tables.Column(accessor='open_date', verbose_name='Opened')
    company = tables.Column(accessor='company')
    cat_no = tables.Column(accessor='cat_num', verbose_name='Catalog #')
    pur_perc = tables.Column(accessor='purity')
    class Meta:
        template_name = 'django_tables2/bootstrap.html'



class LocationTable(tables.Table):
    room = tables.Column(accessor='room')
    name = tables.Column(accessor='name')
    temperature = tables.Column(accessor='temperature')
    description = tables.Column(accessor='description')
    Pois_nv = tables.Column(accessor='ispoison_nonvol')
    pois_vol = tables.Column(accessor='pois_vol')
    react = tables.Column(accessor = 'isreactive')
    flam = tables.Column(accessor='isflammable')
    oxiliq = tables.Column(accessor='isoxidliq')
    baseliq = tables.Column(accessor='isbaseliq')
    orgminacid = tables.Column(accessor='isorgminacid', verbose_name = 'Organic & Mineral Acid')
    oxiacid= tables.Column(accessor='isoxyacid', verbose_name = 'Oxidizing Acid')
    solid = tables.Column(accessor='issolid')
    class Meta:
        template_name = 'django_tables2/bootstrap.html'


class FP_Product_UnitTable(tables.Table):
    house_id = tables.Column(accessor='prod_un.in_house_no', verbose_name='ID')
    desc = tables.Column(accessor='prod_un.description')
    exp = tables.Column(accessor='prod_un.exp_date', verbose_name='Expiration')
    ret = tables.Column(accessor='prod_un.ret_date', verbose_name='Retest')



class Product_Unit_ExpTable(tables.Table):
    class Meta:
        attrs = {'width':'10%'}
        model = Product_Unit
        exclude = ('id', ' is_inactive')
        template_name = 'django_tables2/bootstrap-responsive.html'


class Product_Table(tables.Table):
    class Meta:
        model = Product
        fields = ('name', 'cas', 'min_temp', 'max_temp')
        template_name = 'django_tables2/bootstrap.html'


class User_DeptTable(tables.Table):
    class Meta:
        model = Association
        exclude = ('id', 'user')
        template_name = 'django_tables2/bootstrap-responsive.html'
