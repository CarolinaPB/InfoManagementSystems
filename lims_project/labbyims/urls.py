# Create app specific urls here.

from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
]