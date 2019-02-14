from django.urls import path, include
from . import views
from labbyims.views import search_results
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.no_login, name='no_login'),
    path('login/', auth_views.LoginView.as_view(template_name='labbyims/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('add_product/', views.add_product, name='add_product'),	
    path('add_item/', views.add_item, name='add_item'),
    path('search_results/', search_results.as_view(), name='search_results')

]
