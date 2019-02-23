from django import forms
from django_registration.forms import RegistrationForm
from .models import User

class SignUpForm(RegistrationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    department = forms.CharField(max_length=255, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta(RegistrationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'department', 'email', 'password1', 'password2', )
