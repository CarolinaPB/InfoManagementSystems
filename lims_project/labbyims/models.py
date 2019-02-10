# Create your models here.

from django.db import models


class User(models.Model):
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    department = models.CharField(max_length = 255)


class Product(models.Model):
    cas = models.CharField(max_length = 12)
    name = models.CharField(max_length = 255)
    temperature = models.CharField(max_length = 12)
    ispoison_nonvol = models.BooleanField()
    isreactive = models.BooleanField()
    issolid = models.BooleanField()
    isoxidliq = models.BooleanField()
    isflammable = models.BooleanField()
    isbaseliq = models.BooleanField()
    isorgminacid = models.BooleanField()
    isoxidacid = models.BooleanField()
    ispois_vol = models.BooleanField()


class Product_Unit(models.Model):
    name = models.CharField(max_length = 255)


class Room(models.Model):
    room_name = models.CharField(max_length = 255)

class Location(models.Model):
    description = models.CharField(max_length = 255)
