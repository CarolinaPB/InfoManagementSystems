from django.urls import re_path, path, include
from . import views
from labbyims.views import search_results
from django.contrib.auth import views as auth_views
from django_registration.backends.activation.views import RegistrationView
from .forms import SignUpForm

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.no_login, name='no_login'),
    path('register/', RegistrationView.as_view(form_class=SignUpForm), name='django_registration_register'),
    path('', include('django_registration.backends.activation.urls'), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='labbyims/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add_product/', views.add_product, name='add_product'),	
    path('add_item/', views.add_item, name='add_item')

    # path('search_results/', search_results.as_view(), name='search_results')

]
