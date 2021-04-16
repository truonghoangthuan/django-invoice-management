from django import forms
from django.forms import formset_factory

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
            'customer_name',
            'customer_gender',
            'customer_dob',
        ]
        widgets = {
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
        }


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'customer',
            'date',
        ]
        widgets = {
            'customer': forms.Select(attrs={
                'class': 'form-control',
                'id': 'invoice_customer_name',
                'name': 'invoice_customer_name',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'id': 'invoice_date',
                'placeholder': 'Enter date create',
                'type': 'date',
                'name': 'invoice_date',
            }),
        }


class InvoiceDetailForm(forms.ModelForm):
    class Meta:
        model = InvoiceDetail
        fields = [
            'product',
            'amount',
        ]
        widgets = {
            'product': forms.Select(attrs={
                'class': 'form-control',
                'id': 'invoice_detail_product',
            }),
            'amount': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'invoice_detail_amount',
                'placeholder': 'Enter amount of the product',
                'type': 'number',
            })
        }

InvoiceDetailFormSet = formset_factory(InvoiceDetailForm, extra=1)
