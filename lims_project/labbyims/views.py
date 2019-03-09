from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from labbyims.forms import SignUpForm
from django.template import Context, Template
from django.db.models import F, Q, FloatField
from django.db.models.functions import Cast
from django.views import View
from .forms import AdvancedSearch, Product_UnitForm, Product_Form, \
    Location_Form, Room_Form, Reserve_Form, Update_item_Form, \
    Department_Form, Association_Form, Update_reservation_Form, \
    Update_Location_Form
from .tables import Product_UnitTable, Product_Table, LocationTable, \
    Product_Unit_ExpTable, FP_Product_UnitTable, \
    Product_Unit_MyTable, FP_ReserveTable, ReserveTable, \
    FP_Running_LowTable, Running_LowTable, User_DeptTable
from .models import Product_Unit, Product, Location, Room, Reserve, User,\
    Watching, Department, Association
from django_tables2 import RequestConfig
import datetime
from datetime import datetime, timedelta
from django.utils import timezone
from .filters import ProductFilter, LocationFilter, Prod_ResFilter, UserFilter,\
    DeptFilter, ProductCASFilter
from decimal import Decimal
from django.db import IntegrityError
from django.shortcuts import render_to_response


def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AdvancedSearch(request.POST)
            if form.is_valid():
                search = form.cleaned_data["search"]
                advanced_search = form.cleaned_data["advanced_search"]
                form = AdvancedSearch()
                print(search)
            else:
                print(form.errors)

            c = {'form': form, 'search': search,
                 'advanced_search': advanced_search}

            return render(request, "labbyims/search.html", c)

        else:
            form = AdvancedSearch(initial=request.GET)

        current_date = timezone.now()
        warning = current_date + timedelta(days=27)

        exp_filter = Product_Unit.objects.filter(Q(is_inactive=False),
                                                 Q(exp_date__range=[current_date, warning])
                                                 | Q(ret_date__range =[current_date, warning]) )
        table_exp = FP_Product_UnitTable(exp_filter, prefix="1-")
        RequestConfig(request, paginate={'per_page': 3}).configure(table_exp)

        res_list = Reserve.objects.filter(Q(user_id=request.user),
                                          Q(date_res__range=[current_date, warning])).select_related()
        table_res = FP_ReserveTable(res_list, prefix="2-")
        RequestConfig(request, paginate={'per_page': 3}).configure(table_res)

        watch_list = Watching.objects.filter(Q(prod_un__is_inactive=False),
                                             Q(user_id=request.user), \
                                             #Q(prod_un__prod_perc__lte = 50),\
                                             Q(low_warn=True)).select_related()
        table_low = FP_Running_LowTable(watch_list, prefix='3-')
        RequestConfig(request, paginate={'per_page': 3}).configure(table_low)

        return render(request, 'labbyims/home_afterlogin.html', {'form': form,
                                                                 'table_res': table_res, 'table_exp': table_exp,
                                                                 'table_low': table_low},)
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
    if request.method == "POST" and 'Submit' in request.POST:
        print("getting to POST")
        form = Product_UnitForm(request.POST)
        if form.is_valid():
            number = int(request.POST.get('number', False))
            low_warn_form = form.cleaned_data['low_warn_form']
            dep_id_list = list(request.POST.getlist('department'))
            print(dep_id_list)
            instance = form.save(commit=False)
            for i in range(0, number):
                instance.pk = None
                instance.save()
                j = 0
                if dep_id_list != False:
                    for j in range(0, len(dep_id_list)):
                        dep_id = dep_id_list[j]
                        # print(dep_id)
                        dep = Department.objects.get(pk=dep_id)
                        # print(dep)
                        w = Watching(user=request.user, prod_un=instance,
                                     dept=dep, low_warn=low_warn_form)
                        w.save()
                        j += 1
            return redirect("/home/")
        else:
            print(form.errors)

    else:
        cas_search = request.GET.get('Search', None)
        print(cas_search)
        prod_set = Product.objects.filter(cas=cas_search)
        print(prod_set)
        if not prod_set:
            return render(request, 'labbyims/add_item_cas.html', {'text': "No product with this CAS number was found. Please try again."})
        else:
            for prod in prod_set:
                prod_name = prod.name
                prod_id = prod.id
            form = Product_UnitForm(
                initial={'product': Product.objects.get(pk=prod_id)})

    return render(request, 'labbyims/add_item.html', {'form': form, 'cas': cas_search, 'name': prod_name})


def add_item_cas(request):
    return render(request, 'labbyims/add_item_cas.html')


def inventory(request):
    table = Product_UnitTable(Product_Unit.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'labbyims/inventory.html', {'table': table})


def add_location(request):
    if request.method == "POST":
        form = Location_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('.')
            # return render(request, 'labbyims/home_afterlogin.html')
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
    table_my_inv = Product_Unit_MyTable(Product_Unit.objects.all())
    RequestConfig(request).configure(table_my_inv)
    return render(request, 'labbyims/my_inventory.html', {'table_my_inv': table_my_inv})


def search(request):
    product_list = Product_Unit.objects.all()
    product_list_up = product_list.update(
        curr_amount=F('init_amount') - F('used_amount'))
    product_filter = ProductFilter(request.GET, queryset=product_list)
    return render(request, "labbyims/product_list.html", {'filter': product_filter})


def search_location(request):
    location_list = Location.objects.all()
    location_filter = LocationFilter(request.GET, queryset=location_list)
    return render(request, "labbyims/search_location.html",
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


def add_department(request):
    if request.method == "POST":
        form = Department_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('.')
        else:
            print(form.errors)
    else:
        form = Department_Form()
    context = {'form': form}
    return render(request, 'labbyims/add_department.html', context)


def add_association(request):
    if request.method == "POST":
        try:
            form = Association_Form(request.POST)
            if form.is_valid():
                assoc = form.save(commit=False)
                assoc.user = request.user
                assoc.save()
                return HttpResponseRedirect('.')
            else:
                print(form.errors)
        except IntegrityError:
            return render(request, "labbyims/assoc_error.html", {'form': form})
    else:
        form = Association_Form()
    context = {'form': form}
    return render(request, 'labbyims/add_association.html', context)


def add_reservation(request):
    if request.method == "POST":
        form = Reserve_Form(request.POST)
        if form.is_valid():
            add_res = form.save(commit=False)
            # print(request.user)
            add_res.user = request.user
            add_res.save()
            return HttpResponseRedirect('.')
        else:
            print(form.errors)

    else:
        form = Reserve_Form()

    context = {'form': form}
    return render(request, 'labbyims/add_reservation.html', context)


def reservations(request):
    current_date = timezone.now()
    warning = current_date + timedelta(days=27)
    res_list = Reserve.objects.filter(Q(user_id=request.user),
                                      Q(is_complete=None),
                                      Q(date_res__range=[current_date, warning])).select_related()
    table_res = ReserveTable(res_list)
    RequestConfig(request).configure(table_res)
    return render(request, 'labbyims/reservations.html', {'table_res': table_res, }, )


def running_low(request):
    if request.user.is_authenticated:
        run_low = F('init_amount') / 2

        # prod = Product_Unit.object.get(curr_amount__lte =Cast(\
        # F('init_amount')/2, FloatField()))[0]

        #prod = Product_Unit.objects.get()
        watch_list = Watching.objects.filter(Q(), Q(user_id=request.user),
                                             Q(low_warn=True), Q()).select_related()

        table_watch = Running_LowTable(watch_list)
        RequestConfig(request).configure(table_watch)
        return render(request, 'labbyims/running_low.html', {'table_watch': table_watch, },)
    else:
        return render(request, 'labbyims/home_afterlogin.html')


def about(request):
    return render(request, 'labbyims/about.html')


def running_low(request):
    if request.user.is_authenticated:
        watch_list = Watching.objects.filter(Q(prod_un__is_inactive=False),
                                             Q(user_id=request.user),
                                             Q(low_warn=True)).select_related()
        table_watch = Running_LowTable(watch_list)
        RequestConfig(request).configure(table_watch)
        return render(request, 'labbyims/running_low.html',
                      {'table_watch': table_watch, },)
    else:
        return render(request, 'labbyims/home_afterlogin.html')


def user_info(request):
    if request.user.is_authenticated:

        userprofile = User.objects.filter(id=request.user.id)
        user_filter = UserFilter(request.GET, queryset=userprofile)
        dept_list = Association.objects.filter(user=request.user.id)
        table_dept = User_DeptTable(dept_list)
        user_department = Department.objects.all()
        dept_list = []
        for el in user_department:
            dept_list.append(el.name)
        print(dept_list)
        #user_department = user_department.name
        # print(user_department)
        RequestConfig(request).configure(table_dept)

        return render(request, 'labbyims/user_info.html',
                      {'filter': user_filter, 'table_dept': table_dept, 'dept': dept_list})
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
        expi_date = form.cleaned_data["exp_date"]
        delete = request.POST.getlist("delete_entry")
        archived = request.POST.getlist("is_inactive")
        change_prod_unit = Product_Unit.objects.get(id=prod_units.id)

        if delete:
            change_prod_unit.delete()
        else:
            if used_amount:
                if used_amount > change_prod_unit.curr_amount:
                    pass
                else:
                    change_prod_unit.curr_amount = change_prod_unit.curr_amount - used_amount
                    print(change_prod_unit.curr_amount)
            if retest_date:
                change_prod_unit.ret_date = retest_date
            if opened:
                change_prod_unit.open_date = opened
            if loc:
                change_prod_unit.location = loc
            if expi_date:
                change_prod_unit.exp_date = expi_date
            if archived:
                change_prod_unit.is_inactive = True
            change_prod_unit.save()

        return HttpResponseRedirect('.')
    else:
        form = Update_item_Form()

    return render(request, 'labbyims/update_item.html', {"form": form})


def add_department(request):
    if request.method == "POST":
        form = Department_Form(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('.')
        else:
            print(form.errors)
    else:
        form = Department_Form()
    context = {'form': form}
    return render(request, 'labbyims/add_department.html', context)


def update_reservation(request):
    if request.method == "POST":
        form = Update_reservation_Form(request.POST)
        name = request.POST.get("res")
        amount = request.POST.get("amount_res")
        print(amount)

        try:
            change_res = Reserve.objects.get(res_name=name)
            print(change_res.prod_un.id)
            if change_res:
                change_res.is_complete = True
                change_res.save()
                if amount:
                    change_curr_amount = Product_Unit.objects.get(
                        id=change_res.prod_un.id)
                    change_curr_amount.curr_amount = change_curr_amount.curr_amount - \
                        int(amount)
                    change_curr_amount.save()
                    return HttpResponseRedirect('.')
                else:
                    change_curr_amount = Product_Unit.objects.get(
                        id=change_res.prod_un.id)
                    change_curr_amount.curr_amount = change_curr_amount.curr_amount - change_res.amount_res
                    change_curr_amount.save()
                    return HttpResponseRedirect('.')
        except Exception as e:
            print(e)

    else:
        form = Update_reservation_Form()

        form.fields['res'].queryset = Reserve.objects.filter(
            Q(is_complete=None), Q(user=request.user)).values_list('res_name', flat=True)
        form.fields["amount_res"].label = "Amount used (if left blank it is the same as the reserved amount)"
        form.fields["amount_res"].required = False
        #form.fields["amount_res"].default = Reserve.objects.get()

    return render(request, 'labbyims/update_reservation.html', {"form": form})


def search_advance(request):
    search = request.GET.get('search', None)
    choice = request.GET.get('advanced_search', None)
    if search is not None:
        if choice == 'location':
            location_list = Location.objects.all()
            location_list = location_list.filter(name__contains=search)
            table_se = LocationTable(location_list)
            RequestConfig(request).configure(table_se)
            return render(request, 'labbyims/search_location.html', {'table_se': table_se, }, )

        if choice is None:
            product_list = Product_Unit.objects.all()
            product_list = product_list.filter(description__icontains=search)
            table_se = Product_Unit_MyTable(product_list)
            RequestConfig(request).configure(table_se)
            return render(request, 'labbyims/search_list.html', {'table_se': table_se, },)

        if choice == 'unit':
            product_list = Product_Unit.objects.all()
            product_list = product_list.filter(description__icontains=search)
            table_se = Product_Unit_MyTable(product_list)
            RequestConfig(request).configure(table_se)
            return render(request, 'labbyims/search_list.html', {'table_se': table_se, },)

        if choice == 'product':
            product = Product.objects.all()
            product = product.filter(name__icontains=search)
            table = Product_Table(product)
            RequestConfig(request).configure(table)
            return render(request, 'labbyims/search_product.html', {'table': table, },)


def archive(request):
    amount = Product_Unit.objects.all().annotate(
        amount=F('init_amount') - F('used_amount'))
    amount = amount.filter(amount=0)
    # amount.save(update_fields=['curr_amount'])
    table_arch = Product_Unit_MyTable(amount)
    return render(request, 'labbyims/archive.html', {'table_arch': table_arch, },)


def update_location(request):
    if request.method == "POST":
        form = Update_Location_Form(request.POST)
        if form.is_valid():
            form.save(commit=False)
            loc = request.POST.get("loc")
            new_room = request.POST.get("room")
            descr = request.POST.get("description")

            try:
                n_room = Location.objects.get(id=loc)
                n_room.room = Room.objects.get(id=new_room)
                if descr:
                    n_room.description = descr
                n_room.save()
            except Exception as e:
                print(e)
            return HttpResponseRedirect('.')
        else:
            print(form.errors)

    else:
        form = Update_Location_Form()

    return render(request, 'labbyims/update_location.html', {"form": form})
