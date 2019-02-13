# Create your models here.

from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return User.username

class Product(models.Model):
    cas = models.CharField('CAS number', max_length=12, unique=True)
    name = models.CharField(max_length=255)
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
    product = models.ManyToManyField(Product)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_restricted = models.BooleanField()
    def __str__(self):
        return self.name

class Product_Unit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    reservation = models.ManyToManyField(Account, through='Reserve')
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    is_inactive = models.BooleanField()
    del_date = models.DateField('delivery date')
    open_date = models.DateField('date opened', null=True)
    exp_date = models.DateField('expiration date', null=True)
    ret_date = models.DateField('retest date', null=True)
    purity = models.CharField('purity/percentage', max_length = 255, null=True)
    init_amount = models.DecimalField('initial amount', max_digits=10, decimal_places=4)
    used_amount = models.DecimalField('amount used', max_digits=10, decimal_places=4, default=0)
    company = models.CharField(max_length=255)
    cat_num = models.CharField(max_length=255)
    temperature = models.CharField(max_length=12)
    m_units = models.CharField(max_length = 4)
    def __str__(self):
        return self.name

class Reserve(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    prod_un = models.ForeignKey(Product_Unit, on_delete=models.CASCADE)
    amount_res = models.DecimalField('amount to reserve', max_digits=10, decimal_places=4)
    date_res = models.DateField('date of reservation')
    is_complete = models.BooleanField()
