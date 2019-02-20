from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.views import View
from .forms import AdvancedSearch, BasicSearch, Product_UnitForm
from .models import Product_Unit
from .tables import Product_UnitTable
from django_tables2 import RequestConfig

def home(request):
    if request.method == 'POST':
        #basic_form = BasicSearch(request.POST)
        form = AdvancedSearch(request.POST)
        if form.is_valid():
            search = form.cleaned_data["search"]
            print(search)
        #if basic_form.is_valid():
        #    search = form.cleaned_data["search"]
        #    print(search)

        return HttpResponseRedirect('/home')

    else:
        form = AdvancedSearch(initial=request.GET)
        #basic_form = BasicSearch(initial=request.GET)

    #return render(request, 'labbyims/home_afterlogin.html',{'form':form}, {"basic_form":basic_form})
    return render(request, 'labbyims/home_afterlogin.html',{'form':form})

def no_login(request):
    return render(request, 'labbyims/no_login.html')

def add_product(request):
	return render(request, 'labbyims/add_product.html')

def add_item(request):
    if request.method == "POST":
        form = Product_UnitForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/home')
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
