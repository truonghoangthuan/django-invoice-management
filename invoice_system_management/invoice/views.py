from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.
def index(request):
    return render(request, 'invoice/index.html')

# Product
def create_product(request):
    product = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_product')

    context = {'product': product}

    return render(request, 'invoice/create_product.html', context)


def view_product(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'invoice/view_product.html', context)

# Customer
def create_customer(request):
    customer = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_customer')

    context = {'customer': customer}

    return render(request, 'invoice/create_customer.html', context)


def view_customer(request):
    customer = Customer.objects.all()
    context = {'customer': customer}
    return render(request, 'invoice/view_customer.html', context)

# Invoice detail
def create_invoice_detail(request):
    invoiceDetail = InvoiceDetailForm()

    if request.method == 'POST':
        form = InvoiceDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_invoice_detail')

    context = {'invoiceDetail': invoiceDetail}

    return render(request, 'invoice/create_invoice_detail.html', context)
