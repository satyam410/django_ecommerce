from django.contrib import admin
from .models import Product

# Register your models here.
class ProdcutAdmin(admin.ModelAdmin):
    prepopulated_fields = { 'slug' : ('product_name',)}
    list_display = ('product_name','slug')

admin.site.register(Product, ProdcutAdmin)