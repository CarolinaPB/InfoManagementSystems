from django import forms
from django.db import models
from .models import Product_Unit, Product, Location
from django.forms.widgets import DateInput


class Product_UnitForm(forms.ModelForm):
    class Meta:
        model = Product_Unit
        exclude = ['reservation']
        widgets = {
            "del_date":DateInput(attrs = {"type":"date"}),
            "open_date":DateInput(attrs = {"type":"date"}),
            "exp_date":DateInput(attrs = {"type":"date"}),
            "ret_date":DateInput(attrs = {"type":"date"}),
        }

