from django.forms.widgets import DateInput, Select
from django.core.validators import MinValueValidator
from django import forms
from django_registration.forms import RegistrationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.db import models
from .models import User, Product_Unit, Product, Location, Room, Reserve, Department, Association
from django.forms.widgets import DateInput, TextInput, Select, NumberInput, CheckboxInput
from captcha.fields import ReCaptchaField
from django.db.models import F, Q, FloatField


class SignUpForm(RegistrationForm):
    captcha = ReCaptchaField()
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta(RegistrationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', )

class Product_UnitForm(forms.ModelForm):
    low_warn_form = forms.BooleanField(
        widget=CheckboxInput, label='Running Low Warning (only possible if you choose a department)', initial=False, required=False)
    number = forms.IntegerField(label='How many items with exactly those properties do you want to add to the database?',
                                initial=1, validators=[MinValueValidator(1)])

    class Meta:
        UNIT_CHOICES = (
            ('kg', 'kg'),
            ('l', 'l'),
            ('g', 'g'),
            ('ml', 'ml'),
            ('mg', 'mg'),
            ('µl', 'µl'),
            ('µg', 'µg')
        )
        model = Product_Unit
        exclude = ['reservation', 'is_inactive', 'curr_amount']
        widgets = {
            "del_date": DateInput(attrs={"type": "date"}),
            "open_date": DateInput(attrs={"type": "date"}),
            "exp_date": DateInput(attrs={"type": "date"}),
            "ret_date": DateInput(attrs={"type": "date"}),
            "m_unit": Select(choices=UNIT_CHOICES),
        }


class Product_Form(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class Association_Form(forms.ModelForm):
    #department = forms.ModelChoiceField(queryset=Department.objects.all())

    class Meta:
        model = Association
        exclude = ['user', ]


class Location_Form(forms.ModelForm):
    class Meta:
        model = Location
        fields = "__all__"


class Room_Form(forms.ModelForm):
    class Meta:
        model = Room
        fields = "__all__"


class Department_Form(forms.ModelForm):
    class Meta:
        model = Department
        fields = ["name"]


class Reserve_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Reserve_Form, self).__init__(*args, **kwargs)

    class Meta:
        model = Reserve
        #exclude = ['is_complete',]

        widgets = {
            "date_res": DateInput(attrs={"type": "date"}),
            # 'user': TextInput(),
        }
        exclude = ['user','is_complete', ]
        # fields="__all__"


class Update_item_Form(forms.ModelForm):
    prod_units = forms.ModelChoiceField(
        queryset=Product_Unit.objects.filter(Q(is_inactive=False)), label="Select a unit")
    low_warn_form = forms.BooleanField(
        widget=CheckboxInput, label='Running Low Warning (only possible if you choose a department)', initial=False, required=False)
    # add_department = forms.ModelChoiceField(widget=forms.SelectMultiple,
    #     queryset=Product_Unit.objects.filter(Q(department=None)), label="Associate a department with this unit")

    class Meta:
        model = Product_Unit
        fields = ("prod_units", "in_house_no","used_amount", "open_date",
                  "ret_date", "exp_date", "location","department","low_warn_form" ,"is_inactive")

        widgets = {
            "open_date": DateInput(attrs={"type": "date"}),
            "ret_date": DateInput(attrs={"type": "date"}),
            "exp_date": DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super(Update_item_Form, self).__init__(*args, **kwargs)
        self.fields['location'].required = False
        self.fields['used_amount'].required = False
        #self.fields['add_department'].required =False


class Update_reservation_Form(forms.ModelForm):

    res = forms.ModelChoiceField(
        queryset=Reserve.objects.none(), label="Reservation")
    class Meta:
        model = Reserve
        fields = ["res", "amount_res"]
        def __init__(self, *args, **kwargs):
            super(Update_reservation_Form, self).__init__(*args, **kwargs)
            self.user = kwargs.pop('user', None)

class Update_Location_Form(forms.ModelForm):
    loc = forms.ModelChoiceField(
        queryset=Location.objects.all(), label="Location to change")
    class Meta:
        model = Location
        fields=["loc", "room", "description"]
        #fields=["loc", "room", "description", "ispoison_nonvol", "isreactive", "issolid", "isoxidliq", "isflammable", "isbaseliq", "isorgminacid", "isoxidacid", "ispois_vol"]
