from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'product_name',
            'product_price',
            'product_unit',
        ]
        widgets = {
            'product_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'product_name',
                'placeholder': 'Laptop'
            }),
            'product_price': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'product_price',
                'placeholder': '1000'
            }),
            'product_unit': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'product_unit',
                'placeholder': 'PCS'
            }),
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'customer_name',
            'customer_gender',
            'customer_dob',
            'customer_points'
        ]
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'customer_name',
                'placeholder': 'Nguyen Van A'
            }),
            'customer_gender': forms.Select(attrs={
                'class': 'form-control',
                'id': 'customer_gender'
            }),
            'customer_dob': forms.DateInput(attrs={
                'class': 'form-control',
                'id': 'customer_dob',
                'placeholder': '2000-01-01'
            }),
            'customer_points': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'customer_points',
                'placeholder': 'Points of the customer'
            })
        }

class InvoiceDetailForm(forms.ModelForm):
    class Meta:
        model = InvoiceDetail
        fields = [
            'invoice_detail_product_id',
            'invoice_detail_product_amount',
        ]
        widgets = {
            'invoice_detail_product_id': forms.Select(attrs={
                'class': 'form-control',
                'id': 'product_name',
            }),
            'invoice_detail_product_amount': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'product_price',
                'placeholder': 'Enter amount'
            })
        }
