from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Product, Room, Location, Product_Unit, Reserve, Department, Watching, Association

admin.site.register(User, UserAdmin)
admin.site.register(Product)
admin.site.register(Room)
admin.site.register(Location)
admin.site.register(Product_Unit)
admin.site.register(Reserve)
admin.site.register(Department)
admin.site.register(Watching)
admin.site.register(Association)