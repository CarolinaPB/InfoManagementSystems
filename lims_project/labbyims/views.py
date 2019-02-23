from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.views import View
from .forms import AdvancedSearch, Product_UnitForm, Product_Form, Location_Form
from .models import Product_Unit, Product, Location, Room
from .tables import Product_UnitTable
from django_tables2 import RequestConfig
from .filters import ProductFilter, LocationFilter

def home(request):
    if request.method == 'POST':
        form = AdvancedSearch(request.POST)
        if form.is_valid():
            search_res = form.cleaned_data["search"]
            print(search_res)
        else:
            print(form.errors)

        return HttpResponseRedirect('/search/?description={}'.format(search_res))

    else:
        form = AdvancedSearch(initial=request.GET)
    return render(request, 'labbyims/home_afterlogin.html' ,{'form':form})

def no_login(request):
    return render(request, 'labbyims/no_login.html')

def add_product(request):
    if request.method == "POST":
        form = Product_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('.')
        else:
            print(form.errors)
    else:
        form = Product_Form()

    context = {'form': form}
    return render(request, 'labbyims/add_product.html', context)

def add_item(request):
    if request.method == "POST":
        form = Product_UnitForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('.')
            #return render(request, 'labbyims/home_afterlogin.html')
        else:
            print(form.errors)
    else:
        form = Product_UnitForm()

    context = {'form': form}
    return render(request, 'labbyims/add_item.html', context)

def search_results(request):
    table = Product_UnitTable(Product_Unit.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'labbyims/results.html', {'table': table})

def add_location(request):
    if request.method == "POST":
        form = Location_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('.')
            #return render(request, 'labbyims/home_afterlogin.html')
        else:
            print(form.errors)
    else:
        form = Location_Form()

    context = {'form': form}
    return render(request, 'labbyims/add_location.html', context)

def locations(request):
    return render(request, 'labbyims/locations.html')


def search(request):
    product_list = Product_Unit.objects.all()
    product_filter = ProductFilter(request.GET, queryset=product_list)
    return render(request, "labbyims/product_list.html", {'filter': product_filter})

def search_location(request):
	    location_list = Location.objects.all()
	    location_filter = LocationFilter(request.GET, queryset=location_list)
	    return render(request, "labbyims/search_location.html", {'filter': location_filter})
