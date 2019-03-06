from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal
from django.core.validators import MinValueValidator


class User(AbstractUser):
    pass

class Product(models.Model):
    cas = models.CharField('CAS number', max_length=12, unique=True)
    name = models.CharField(max_length=255)
    min_temp = models.DecimalField('Maximum Temperature', max_digits=10, decimal_places=4, default = 25)
    max_temp = models.DecimalField('Minimum Temperature', max_digits=10, decimal_places=4, default = 25)
    ispoison_nonvol = models.BooleanField('is poison - non-volatile')
    isreactive = models.BooleanField('is reactive')
    issolid = models.BooleanField('is solid')
    isoxidliq = models.BooleanField('is oxidizing liquid')
    isflammable = models.BooleanField('is flammable')
    isbaseliq = models.BooleanField('is base liquid')
    isorgminacid = models.BooleanField('is organic and mineral acid')
    isoxidacid = models.BooleanField('is oxidizing acid')
    ispois_vol = models.BooleanField('is poison - volatile')
    def __str__(self):
        return self.name

class Room(models.Model):
    room_name = models.CharField(max_length=255)
    building_name = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.room_name

class Location(models.Model):
    # product = models.ManyToManyField(Product)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    ispoison_nonvol = models.BooleanField('is poison - non-volatile', default = False)
    isreactive = models.BooleanField('is reactive', default = False)
    issolid = models.BooleanField('is solid', default = False)
    isoxidliq = models.BooleanField('is oxidizing liquid', default = False)
    isflammable = models.BooleanField('is flammable', default = False)
    isbaseliq = models.BooleanField('is base liquid', default = False)
    isorgminacid = models.BooleanField('is organic and mineral acid', default = False)
    isoxidacid = models.BooleanField('is oxidizing acid', default = False)
    ispois_vol = models.BooleanField('is poison - volatile', default = False)
    def is_valid(self, Product):
        if (self.ispois_vol == Product.ispoison_nonvol and self.ispoison_nonvol == Product.ispoison_nonvol and self.issolid == Product.issolid):
            return True
        else:
            return False
    def __str__(self):
        return self.name

class Department(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Product_Unit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    in_house_no = models.CharField('In House ID', max_length=255, blank = True )
    del_date = models.DateField('delivery date')
    company = models.CharField(max_length=255)
    cat_num = models.CharField('catalog number', max_length=255, blank = True)
    description = models.CharField(max_length=255)
    batch = models.CharField('Batch Number', max_length=255, blank = True )
    init_amount = models.DecimalField('initial amount', max_digits=10, decimal_places=4, default = 0, validators = [MinValueValidator(0.0000)])
    m_unit = models.CharField('measuring units', max_length=4, null=True, blank = True)
    purity = models.CharField('purity/percentage', max_length = 255, null=True, blank = True)
    exp_date = models.DateField('expiration date', null=True, blank = True)
    ret_date = models.DateField('retest date', null=True, blank = True)
    open_date = models.DateField('date opened', null=True, blank = True)
    used_amount = models.DecimalField('amount used', max_digits=10, decimal_places=4, default=0, validators = [MinValueValidator(0.0000)])
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    reservation = models.ManyToManyField(User, through='Reserve')
    is_inactive = models.BooleanField('Archived', default = False)
    curr_amount = models.DecimalField('current amount', max_digits=10, decimal_places=4, default=0, blank = True, validators = [MinValueValidator(0.0000)])
    watch = models.ManyToManyField(Department, through='Watching')
    def curr_am(self):
        init = float(self.init_amount)
        used = float(self.used_amount)
        return init - used
    def perc_left(self):
        current = self.curr_am()
        initial = float(self.init_amount)
        return (current/initial)*100
    def __str__(self):
        return self.description

class Reserve(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prod_un = models.ForeignKey(Product_Unit, verbose_name='description', on_delete=models.CASCADE)
    amount_res = models.DecimalField('amount to reserve', max_digits=10, decimal_places=4)
    date_res = models.DateField('date of reservation')
    is_complete = models.BooleanField()

class Uses(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    prod_un = models.ForeignKey(Product_Unit, verbose_name='description',  on_delete=models.CASCADE)
    amount_used = models.DecimalField('amount used', max_digits=10, decimal_places=4)
    date_used = models.DateField('date of use')

class Watching(models.Model):
    user = models.ForeignKey(User, default=0, on_delete=models.CASCADE)
    prod_un = models.ForeignKey(Product_Unit, on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    low_warn = models.BooleanField('Running Low Warning')
    prod_perc = models.DecimalField('Percent left', default = 100, max_digits=10, decimal_places=4)
    def save(self, *args, **kwargs):
        self.prod_perc = (self.prod_un.curr_amount/self.prod_un.init_amount)*100
        super(Watching, self).save(*args, **kwargs)
    def __str__(self):
        return self.low_warn
