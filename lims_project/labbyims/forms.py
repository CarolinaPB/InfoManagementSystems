from django import forms
from django_registration.forms import RegistrationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.db import models
from .models import User, Product_Unit, Product, Location, Room, Reserve
from django.forms.widgets import DateInput, TextInput
from captcha.fields import ReCaptchaField


class SignUpForm(RegistrationForm):
    captcha = ReCaptchaField()
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta(RegistrationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class AdvancedSearch(forms.Form):
    search = forms.CharField(widget=forms.TextInput(attrs={'class': 'col-md-12 searchfield'}), label=False)
    CHOICES=[
             ('unit', 'Unit'),
             ('location','Location'),
             ('item_type','Item type'),
             ('finished', 'Finished')
             ]
    advanced_search = forms.ChoiceField(choices=CHOICES, label=False)
    advanced_search.widget.attrs.update({'class': 'col-md-6'})
    advanced_search.widget.attrs.update({'name': 'advanced_search'})
    advanced_search.widget.attrs.update({'id': 'advanced_search'})
    #search.widget.attrs.update({'action': '/search/'})
    search.widget.attrs.update({'name': 'description'})
    search.widget.attrs.update({'type': 'search'})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        #self.helper.form_method = "post='/search/'"

        self.helper.layout = Layout(
            "search",
            "advanced_search",
            Submit("submit", "Search", css_class="btn")
        )

class Product_UnitForm(forms.ModelForm):
    class Meta:
        model = Product_Unit
        exclude = ['reservation']
        widgets = {
            "del_date":DateInput(attrs = {"type":"date"}),
            "open_date":DateInput(attrs = {"type":"date"}),
            "exp_date":DateInput(attrs = {"type":"date"}),
            "ret_date":DateInput(attrs = {"type":"date"}),
        }

class Product_Form(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class Location_Form(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"

class Room_Form(forms.ModelForm):
    class Meta:
        model = Room
        fields="__all__"

class Reserve_Form(forms.ModelForm):
    class Meta:
        model=Reserve
        exclude = ['is_complete']
        widgets = {
            "date_res":DateInput(attrs = {"type":"date"}),
            'user': TextInput(attrs={'readonly': 'readonly'}),
        }
        #fields="__all__"
