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


# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = [
#             'customer_name',
#             'customer_gender',
#             'customer_dob',
#         ]
#         widgets = {
#             'customer_name': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'id': 'customer_name',
#                 'placeholder': 'Enter name of the customer',
#             }),
#             'customer_gender': forms.Select(attrs={
#                 'class': 'form-control',
#                 'id': 'customer_gender',
#             }),
#             'customer_dob': forms.DateInput(attrs={
#                 'class': 'form-control',
#                 'id': 'customer_dob',
#                 'placeholder': '2000-01-01',
#                 'type': 'date',
#             }),
#         }


class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'customer',
            'comments',
            'contact',
            'email',
        ]
        widgets = {
            'customer': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'invoice_customer',
                'placeholder': 'Enter name of the customer',
            }),
            'contact': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'invoice_contact',
                'placeholder': 'Enter contact of the customer',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'invoice_email',
                'placeholder': 'Enter email of the customer',
            }),
            'comments': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'invoice_comments',
                'placeholder': 'Enter comments',
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
                'placeholder': '0',
                'type': 'number',
            })
        }


class excelUploadForm(forms.Form):
    file = forms.FileField()


InvoiceDetailFormSet = formset_factory(InvoiceDetailForm, extra=1)
