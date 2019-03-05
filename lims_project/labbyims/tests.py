# Create your tests here.

from django.test import TestCase
from labbyims.models import Room, Location, Product, Product_Unit

class DatabaseTestCase(TestCase):
    pass
    """def location_check(self):
        room_01 = Room(room_name='Lab_0', building_name='BMC')
        Location_01 = Location(name='cabinet_01',description='Nice cabinet', ispoison_nonvol=False,isreactive=False, issolid=False,isoxidliq=False,isflammable=False,isbaseliq=False,isorgminacid=False, isoxidacid=False,ispois_vol=False, room_id=1)
        Product_01 = Product(cas='7732-18-5',name='Water',ispoison_nonvol=False,isreactive=False, issolid=False,isoxidliq=False,isflammable=False,isbaseliq=False,isorgminacid=False, isoxidacid=False,ispois_vol=False, min_temp='17', max_temp='25')
        Product_Unit_01 = Product_Unit(description='3L Flask ddH2O',is_inactive=False,del_date='2019-02-12', exp_date='2019-08-12',purity='',init_amount='3000',used_amount='100',curr_amount='2900',company='Made in House', cat_num='',location_id=1,product_id=1, m_unit = 'mL')
        Product_Unit_02 = Product_Unit(description='100mL Flask ddH2O',is_inactive=False, del_date='2019-02-15', exp_date='2019-08-15',purity='',init_amount='100',used_amount='0', curr_amount='100', company='Made in House', cat_num='',location_id=1,product_id=1, m_unit = 'mL')
        self.assertIs(Location_01.is_valid(Product_Unit_01), True)"""

