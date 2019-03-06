# Create your views here.

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from labbyims.forms import SignUpForm
from django.template import Context, Template

from django.db.models import F,Q, FloatField
from django.db.models.functions import Cast

from django.views import View
from .forms import AdvancedSearch, Product_UnitForm, Product_Form, Location_Form, Room_Form, Reserve_Form, Update_item_Form
from .tables import Product_UnitTable, LocationTable, Product_Unit_ExpTable, FP_Product_UnitTable, Product_Unit_MyTable, FP_ReserveTable, ReserveTable, FP_Running_LowTable, Running_LowTable, User_info_table
from .models import Product_Unit, Product, Location, Room, Reserve, User, Watching, Department
from django_tables2 import RequestConfig
import datetime
from datetime import datetime, timedelta
from django.utils import timezone
from .filters import ProductFilter, LocationFilter, Prod_ResFilter, ProductCASFilter, UserFilter, DeptFilter
from decimal import Decimal


def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AdvancedSearch(request.POST)
            if form.is_valid():
                search_res = form.cleaned_data["search"]
            else:
                print(form.errors)

            return HttpResponseRedirect('/search/?description={}'.format(search_res))

        else:
            form = AdvancedSearch(initial=request.GET)

        current_date = timezone.now()
        warning = current_date + timedelta(days=27)

        exp_filter = Product_Unit.objects.filter(Q(is_inactive=False), \
                    Q(is_inactive = False), \
                    Q(exp_date__range = [current_date, warning ]) | \
                    Q(ret_date__range =[current_date, warning ]) )
        table_exp = FP_Product_UnitTable(exp_filter, prefix="1-")
        RequestConfig(request,paginate={'per_page': 3} ).configure(table_exp)

        res_list=Reserve.objects.filter(Q(prod_un__is_inactive = False),\
                    Q(user_id= request.user),Q(date_res__range = \
                    [current_date, warning ])).select_related()
        table_res = FP_ReserveTable(res_list, prefix="2-")
        RequestConfig(request,paginate = {'per_page': 3}).configure(table_res)

        watch_list = Watching.objects.filter(Q(prod_un__is_inactive = False), \
                    Q(user_id= request.user), \
                    Q(low_warn = True)).select_related()
        table_low = FP_Running_LowTable(watch_list, prefix='3-')
        RequestConfig(request,paginate = {'per_page': 3}).configure(table_low)

        return render(request, 'labbyims/home_afterlogin.html',{'form':form, \
                    'table_res':table_res, 'table_exp': table_exp, \
                    'table_low':table_low},)
    else:
        return render(request, 'labbyims/home_afterlogin.html')



def no_login(request):
    return render(request, 'labbyims/no_login.html')

def add_product(request):
    if request.method == "POST":
        form = Product_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('.')
        else:
            print(form.errors)
    else:
        form = Product_Form()

    context = {'form': form}
    return render(request, 'labbyims/add_product.html', context)


def add_item(request):
    if request.method == "POST":
        form = Product_UnitForm(request.POST)
        number = request.POST.get('number', False)
        number = int(number)
        if form.is_valid():
            instance = form.save(commit=False)
            for i in range(0, number):
                instance.pk = None
                instance.save()
            return HttpResponseRedirect('.')
            #return render(request, 'labbyims/home.html')
        else:
            print(form.errors)
    else:
        form = Product_UnitForm()

    return render(request, 'labbyims/add_item.html', {'form': form})

def add_item_cas(request):
    if request.method == "POST":
        product_list = Product.objects.all()
        product_filter = ProductCASFilter(request.GET, queryset=product_list)
        print(product_filter)
        return render(request, "labbyims/add_item.html", {'filter': product_filter})
    else:
        return render(request, 'labbyims/add_item_cas.html')

def inventory(request):
    inv_filter = Product_Unit.objects.filter(is_inactive = False)
    table = Product_UnitTable(inv_filter)
    RequestConfig(request).configure(table)
    return render(request, 'labbyims/inventory.html', {'table': table})


def add_location(request):
    if request.method == "POST":
        form = Location_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('.')
            #return render(request, 'labbyims/home_afterlogin.html')
        else:
            print(form.errors)
    else:
        form = Location_Form()

    context = {'form': form}
    return render(request, 'labbyims/add_location.html', context,)


def locations(request):
    table_1 = LocationTable(Location.objects.all())
    RequestConfig(request).configure(table_1)
    return render(request, 'labbyims/locations.html', {'table_1': table_1})

def my_inventory(request):
    my_inv_filter = Product_Unit.objects.filter(is_inactive = False)
    table_my_inv = Product_Unit_MyTable(my_inv_filter)
    RequestConfig(request).configure(table_my_inv)
    return render(request, 'labbyims/my_inventory.html', \
                {'table_my_inv': table_my_inv})

def search(request):
    product_list = Product_Unit.objects.all()
    product_list_up = product_list.update(curr_amount=F('init_amount')- \
                    F('used_amount'))
    product_filter = ProductFilter(request.GET, queryset=product_list)
    return render(request, "labbyims/product_list.html", \
                {'filter': product_filter})

def search_location(request):
    location_list = Location.objects.all()
    location_filter = LocationFilter(request.GET, queryset=location_list)
    return render(request, "labbyims/search_location.html",\
                {'filter': location_filter})

def add_room(request):
    if request.method == "POST":
        form = Room_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('.')
        else:
            print(form.errors)
    else:
        form = Room_Form()

    context = {'form': form}
    return render(request, 'labbyims/add_room.html', context)

def add_reservation(request):
    if request.method == "POST":
        form = Reserve_Form(request.POST)
        add_res = form.save(commit=False)
        print(request.user)
        add_res.user = request.user
        add_res.save()
        return HttpResponseRedirect('.')
    else:
        form = Reserve_Form()

    context = {'form': form}
    return render(request, 'labbyims/add_reservation.html', context)

def reservations(request):
    current_date = timezone.now()
    warning = current_date + timedelta(days=27)
    res_list=Reserve.objects.filter(Q(user_id= request.user),\
                    Q(date_res__range = [current_date, \
                    warning ])).select_related()
    table_res = ReserveTable(res_list)
    RequestConfig(request).configure(table_res)
    return render(request, 'labbyims/reservations.html', \
                {'table_res': table_res,}, )

def running_low(request):
    if request.user.is_authenticated:
        watch_list = Watching.objects.filter(Q(prod_un__is_inactive = False), \
                    Q(user_id= request.user), \
                    Q(low_warn = True)).select_related()
        table_watch = Running_LowTable(watch_list)
        RequestConfig(request).configure(table_watch)
        return render(request, 'labbyims/running_low.html', \
                    {'table_watch':table_watch,},)
    else:
        return render(request, 'labbyims/home_afterlogin.html')

def about(request):
    return render(request, 'labbyims/about.html')

def user_page(request):
    #print(request.user)
    #user_list = User.objects.all()
    #user_table=User_info_table(user_list)
    #RequestConfig(request).configure(user_table)

    #user_list = User.objects.all()
    #user_filter = User(request.GET, queryset=user_list)
    #print(user_filter)

    #print (User.username)
    #return render(request, 'labbyims/user_page.html', {'filter':user_filter})

    t = Template('This is your <span>{{ message }}</span>.')
    c = Context({'message': 'Your message'})
    html = t.render(c)


    return render(request, 'labbyims/user_page.html', html)

def user_info(request):
    if request.user.is_authenticated:

        userprofile = User.objects.filter(id= request.user.id)
        user_filter = UserFilter(request.GET, queryset=userprofile)

        user_dept = Department.objects.filter(user = request.user.id)
        dept_filter = UserFilter(request.GET, queryset=user_dept)

        return render(request, 'labbyims/user_info.html', {'filter':user_filter}, {'filter':dept_filter})
    else:
        return render(request, 'labbyims/home_afterlogin.html')

def update_item(request):
    if request.method == "POST":
        form = Update_item_Form(request.POST)
        edit = form.save(commit=False)

        prod_units = form.cleaned_data["prod_units"]
        used_amount = form.cleaned_data["used_amount"]
        retest_date = form.cleaned_data["ret_date"]
        opened = form.cleaned_data["open_date"]
        loc = form.cleaned_data["location"]
        print(prod_units)
        print(used_amount)
        print(retest_date)
        unit = Product_Unit.objects.get(description=prod_units)
        change_prod_unit = Product_Unit.objects.get(id=unit.id)

        if used_amount:
            if used_amount > change_prod_unit.curr_amount:
                pass
            else:
                change_prod_unit.curr_amount = change_prod_unit.curr_amount - used_amount
                print(change_prod_unit.curr_amount)
                #change_prod_unit.save()
        if retest_date:
            change_prod_unit.ret_date = retest_date

        if opened:
            change_prod_unit.open_date = opened
        if loc:
            change_prod_unit.location = loc

        change_prod_unit.save()



        return HttpResponseRedirect('.')
    else:
        form = Update_item_Form()


    return render(request, 'labbyims/update_item.html', {"form":form})

    model = User
    template_name = 'labbyims/user_page.html'
    def get_queryset():
        return User.objects.all()
    u = get_queryset()
    print (u)
    context={'user':u}

    return render(request, 'labbyims/user_page.html', context)
