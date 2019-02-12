# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

from django.views import View

def home(request):
    return render(request, 'labbyims/base.html')



class search_results(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('LEROY JEKiNSSSSSSSS')
