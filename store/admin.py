from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'slug', 'date_created', 'date_modified')
    prepopulated_fields = {'slug': ('product_name',)}
    

admin.site.register(Product, ProductAdmin)
