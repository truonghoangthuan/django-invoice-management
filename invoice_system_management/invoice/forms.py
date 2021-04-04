from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            # 'product_id',
            'product_name',
            'product_price',
            'product_unit',
        ]
        widgets = {
            # 'product_id': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'id': 'product_id',
            #     'placeholder': 'Enter ID for the product',
            # }),
            'product_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'product_name',
                'placeholder': 'Enter name of the product',
            }),
            'product_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'product_price',
                'placeholder': 'Enter price of the product',
                'type': 'number',
            }),
            'product_unit': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'product_unit',
                'placeholder': 'Enter unit of the product',
            }),
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            # 'customer_id',
            'customer_name',
            'customer_gender',
            'customer_dob',
            'customer_points',
        ]
        widgets = {
            # 'customer_id': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'id': 'customer_id',
            #     'placeholder': 'Enter ID of the customer',
            # }),
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'customer_name',
                'placeholder': 'Enter name of the customer',
            }),
            'customer_gender': forms.Select(attrs={
                'class': 'form-control',
                'id': 'customer_gender',
            }),
            'customer_dob': forms.DateInput(attrs={
                'class': 'form-control',
                'id': 'customer_dob',
                'placeholder': '2000-01-01',
                'type': 'date',
            }),
            'customer_points': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'customer_points',
                'placeholder': 'Enter points of the customer',
                'type': 'number',
            })
        }


class InvoiceDetailForm(forms.ModelForm):
    class Meta:
        model = InvoiceDetail
        fields = [
            # 'invoice_detail_id',
            'invoice_detail_product_name',
            'invoice_detail_product_amount',
        ]
        widgets = {
            # 'invoice_detail_id': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'id': 'invoice_detail_id',
            #     'placeholder': 'Enter ID of the bill',
            # }),
            'invoice_detail_product_name': forms.Select(attrs={
                'class': 'form-control',
                'id': 'invoice_detail_product_name',
            }),
            'invoice_detail_product_amount': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'invoice_detail_product_amount',
                'placeholder': 'Enter amount of the product',
                'type': 'number',
            })
        }


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            # 'invoice_id',
            'invoice_customer_name',
            'invoice_date',
            # 'invoice_total',
        ]
        widgets = {
            # 'invoice_id': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'id': 'invoice_detail_id',
            # }),
            'invoice_customer_name': forms.Select(attrs={
                'class': 'form-control',
                'id': 'invoice_customer_name',
            }),
            'invoice_date': forms.DateInput(attrs={
                'class': 'form-control',
                'id': 'invoice_date',
                'placeholder': 'Enter date create',
                'type': 'date',
            }),
            # 'invoice_total': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'id': 'invoice_total',
            #     'placeholder': 'Total bill',
            #     'type': 'number',
            # }),
        }
