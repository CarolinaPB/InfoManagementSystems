# Create app specific urls here.

from django.urls import path, include

from . import views

from labbyims.views import search_results

urlpatterns = [
    path('', views.home, name='home'),

    path('search_results/', search_results.as_view(), name='search_results')

]
