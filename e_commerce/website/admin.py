from django.contrib import admin
from .models import AuthUser, Products, Categories, Customers

admin.site.register(Products)
admin.site.register(Categories)
admin.site.register(Customers)
admin.site.register(AuthUser)
