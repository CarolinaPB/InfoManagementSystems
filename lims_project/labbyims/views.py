from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.views import View
from .forms import AdvancedSearch, Product_UnitForm, Product_Form, Location_Form
from .models import Product_Unit, Product
from .tables import Product_UnitTable
from django_tables2 import RequestConfig

def home(request):
    if request.method == 'POST':
        form = AdvancedSearch(request.POST)
        if form.is_valid():
            search_res = form.cleaned_data["search"]
            print(search_res)
            print(Product.objects.search(search))
        else:
            print(form.errors)

        return HttpResponseRedirect('/home')

    else:
        form = AdvancedSearch(initial=request.GET)
    return render(request, 'labbyims/home_afterlogin.html',{'form':form})

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

<<<<<<< HEAD
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

<<<<<<< HEAD
    context = {'form': form}
    return render(request, 'labbyims/add_item.html', context)
=======
=======
>>>>>>> parent of 5c0b928... Search option
#class search_results(View):

#    def get(self, request, *args, **kwargs):
#        return render(request, 'labbyims/results.html')
<<<<<<< HEAD
>>>>>>> parent of 5c0b928... Search option
=======
>>>>>>> parent of 5c0b928... Search option

def search_results(request):
    table = Product_UnitTable(Product_Unit.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'labbyims/results.html', {'table': table})
<<<<<<< HEAD
<<<<<<< HEAD

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
=======
>>>>>>> parent of 5c0b928... Search option
=======
>>>>>>> parent of 5c0b928... Search option
