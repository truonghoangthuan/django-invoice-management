from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.
def base(request):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
    }

    return render(request, 'invoice/base/base.html', context)

# Home view


def index(request):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
    }
    return render(request, 'invoice/index.html', context)

# Product view


def create_product(request):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()

    product = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_product')

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
        'product': product,
    }

    return render(request, 'invoice/create_product.html', context)


def view_product(request):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()

    product = Product.objects.all()

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
        'product': product,
    }

    return render(request, 'invoice/view_product.html', context)

# Customer view


def create_customer(request):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()

    customer = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_customer')

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
        'customer': customer,
    }

    return render(request, 'invoice/create_customer.html', context)


def view_customer(request):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()

    customer = Customer.objects.all()

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
        'customer': customer,
    }

    return render(request, 'invoice/view_customer.html', context)

# Invoice detail view


def create_invoice_detail(request):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()

    invoiceDetail = InvoiceDetailForm()
    invoice = InvoiceForm()

    if request.method == 'POST':
        form = InvoiceDetailForm(request.POST)
        if form.is_valid():
            form.save()

            form2 = InvoiceForm()
            if form2.is_valid():
                form2.save()
                return redirect('create_invoice_detail')

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
        'invoiceDetail': invoiceDetail,
        'invoice': invoice
    }

    return render(request, 'invoice/create_invoice_detail.html', context)

# Invoice view


def view_invoice(request):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()

    invoice = Invoice.objects.all()

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
        'invoice': invoice,
    }

    return render(request, 'invoice/view_invoice.html', context)
