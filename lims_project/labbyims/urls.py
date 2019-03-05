from django.urls import re_path, path, include
from . import views
from django.contrib.auth import views as auth_views
from django_registration.backends.activation.views import RegistrationView
from .forms import SignUpForm

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('register/', RegistrationView.as_view(form_class=SignUpForm), name='django_registration_register'),
    path('', include('django_registration.backends.activation.urls'), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='labbyims/login.html'), name='login'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='labbyims/password_change.html'), name='password_change'),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='labbyims/password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='labbyims/password_reset.html', email_template_name='labbyims/password_reset_email.html', subject_template_name='labbyims/password_reset_subject.txt'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='labbyims/password_reset_done.html'), name='password_reset_done'),
    re_path(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(template_name='labbyims/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='labbyims/password_reset_complete.html'), name='password_reset_complete'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('inventory/', views.inventory, name='inventory'),
    path('add_product/', views.add_product, name='add_product'),
    path('add_item/', views.add_item, name='add_item'),
    path('add_location/', views.add_location, name='add_location'),
    path('locations/', views.locations, name='locations'),
    path('my_inventory/', views.my_inventory, name='my_inventory'),
    re_path(r'^search/$',views.search,name='search'),
    re_path(r'^search_location/$',views.search_location, name='search_location'),
    path('add_room/', views.add_room, name='add_room'),
    path('add_reservation/', views.add_reservation, name='add_reservation'),
    path('reservations/', views.reservations, name='reservations'),
    path('about/', views.about, name='about'),
    path('running_low/', views.running_low, name='running_low'),
    path('user_info/', views.user_info, name = 'user_info')
]
