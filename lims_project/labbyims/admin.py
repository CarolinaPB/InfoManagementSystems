from django.contrib import admin
from .models import Account, Product, Room, Location, Product_Unit, Reserve

admin.site.register(Account)
admin.site.register(Product)
admin.site.register(Room)
admin.site.register(Location)
admin.site.register(Product_Unit)
admin.site.register(Reserve)
