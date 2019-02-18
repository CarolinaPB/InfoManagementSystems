# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

from django.views import View
from .forms import Product_UnitForm
from .models import Product_Unit


def home(request):
    return render(request, 'labbyims/home_afterlogin.html')

def no_login(request):
    return render(request, 'labbyims/no_login.html')

def add_product(request):
	return render(request, 'labbyims/add_product.html')
	
def add_item(request):
    if request.method == "POST":
        form = Product_UnitForm(request.POST or None)
        if form.is_valid():
            form.save(commit=True)
            return render(request, 'labbyims/home_afterlogin.html')
        else:
            print(form.errors)
    else:
        form = Product_UnitForm()
    
    context = {'form': form}     
    return render(request, 'labbyims/add_item.html', context)

	
class search_results(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'labbyims/results.html')
		
		
