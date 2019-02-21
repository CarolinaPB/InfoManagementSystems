# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Product_Unit
from .tables import Product_UnitTable
from django_tables2 import RequestConfig
from django.db.models import Q
from labbyims.models import Product_Unit
from labbyims.models import Product_Unit
from django.shortcuts import render
from .filters import ProductFilter

def home(request):
    return render(request, 'labbyims/home_afterlogin.html')

def no_login(request):
    return render(request, 'labbyims/no_login.html')

def add_product(request):
	return render(request, 'labbyims/add_product.html')

def add_item(request):
	return render(request, 'labbyims/add_item.html')



def search_results(request):
    table = Product_UnitTable(Product_Unit.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'labbyims/results.html', {'table': table})


def search(request):
    product_list = Product_Unit.objects.all()
    product_filter = ProductFilter(request.GET, queryset=product_list)
    return render(request, "labbyims/product_list.html", {'filter': product_filter})