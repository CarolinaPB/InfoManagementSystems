# Create your views here.

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from labbyims.forms import SignUpForm
from django.views import View

def home(request):
    return render(request, 'labbyims/home_afterlogin.html')

def no_login(request):
    return render(request, 'labbyims/no_login.html')

def add_product(request):
	return render(request, 'labbyims/add_product.html')
	
def add_item(request):
	return render(request, 'labbyims/add_item.html')

def search_results(request):
    return render(request, 'labbyims/results.html')

def account_activation_sent(request):
    return render(request, 'labbyims/account_activation_sent.html')


"""class search_results(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'labbyims/results.html')"""
