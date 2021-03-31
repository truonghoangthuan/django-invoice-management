from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'product_price', 'product_unit']
    
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'customer_gender', 'customer_dob', 'customer_points']
    
class InvoiceDetailAdmin(admin.ModelAdmin):
    list_display = ['id', 'invoice_detail_product_id', 'invoice_detail_product_amount']

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'invoice_date', 'invoice_total', 'customer_id']

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(InvoiceDetail, InvoiceDetailAdmin)
admin.site.register(Invoice, InvoiceAdmin)
