from django.urls import re_path, path, include
from . import views
from django.contrib.auth import views as auth_views
from django_registration.backends.activation.views import RegistrationView
from .forms import SignUpForm

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.no_login, name='no_login'),
    path('register/', RegistrationView.as_view(form_class=SignUpForm), name='django_registration_register'),
    path('', include('django_registration.backends.activation.urls'), name='signup'),
    path('home/login/', auth_views.LoginView.as_view(template_name='labbyims/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('inventory/', views.inventory, name='inventory'),
    path('add_product/', views.add_product, name='add_product'),	
    path('add_item/', views.add_item, name='add_item'),
    path('add_location/', views.add_location, name='add_location'),
    path('locations/', views.locations, name='locations'),
    path('expiring_retesting/', views.expiring, name='expiring_retesting'),
    re_path(r'^search/$',views.search,name='search'),
    re_path(r'^search_location/$',views.search_location, name='search_location'),
    path('add_room/', views.add_room, name='add_room'),
    path('add_reservation/', views.add_reservation, name='add_reservation'),
    path('reservations/', views.reservations, name='reservations'),
]
