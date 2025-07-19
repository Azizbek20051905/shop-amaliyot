from django.contrib import admin
from .models import Category, CustomeUser, Cart, Order, Product

# Register your models here.
admin.site.register(CustomeUser)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Product)