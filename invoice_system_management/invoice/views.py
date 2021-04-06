from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *


# Create your views here.
def base(request):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
        'total_invoice': total_invoice,
    }

    return render(request, 'invoice/base/base.html', context)

# Home view


def index(request):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
        'total_invoice': total_invoice,
    }
    return render(request, 'invoice/index.html', context)

# Product view


def create_product(request):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()

    product = ProductForm()

    if request.method == 'POST':
        product = ProductForm(request.POST)
        if product.is_valid():
            product.save()
            return redirect('create_product')

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
        'total_invoice': total_invoice,

        'product': product,
    }

    return render(request, 'invoice/create_product.html', context)


def view_product(request):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()

    product = Product.objects.all()

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
        'total_invoice': total_invoice,

        'product': product,
    }

    return render(request, 'invoice/view_product.html', context)

# Customer view


def create_customer(request):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()

    customer = CustomerForm()

    if request.method == 'POST':
        customer = CustomerForm(request.POST)
        if customer.is_valid():
            customer.save()
            return redirect('create_customer')

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
        'total_invoice': total_invoice,

        'customer': customer,
    }

    return render(request, 'invoice/create_customer.html', context)


def view_customer(request):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()

    customer = Customer.objects.all()

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
        'total_invoice': total_invoice,

        'customer': customer,
    }

    return render(request, 'invoice/view_customer.html', context)


# Invoice view

def create_invoice(request):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()

    invoice = InvoiceForm()

    if request.method == 'POST':
        invoice = InvoiceForm(request.POST)
        if (invoice.is_valid()):
            invoice.save()
            return redirect('create_invoice')

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
        'total_invoice': total_invoice,

        'invoice': invoice,
    }

    return render(request, 'invoice/create_invoice.html', context)


def view_invoice(request):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()

    invoice = Invoice.objects.all()

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
        'total_invoice': total_invoice,

        'invoice': invoice,
    }

    return render(request, 'invoice/view_invoice.html', context)

# Invoice detail view


def create_invoice_detail(request):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()

    invoice_detail = InvoiceDetailForm()

    if request.method == 'POST':
        invoice_detail = InvoiceDetailForm(request.POST)
        if (invoice_detail.is_valid()):
            invoice_detail.save()
            return redirect('create_invoice_detail')

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
        'total_invoice': total_invoice,

        'invoice_detail': invoice_detail,
    }

    return render(request, 'invoice/create_invoice_detail.html', context)


def view_invoice_detail(request, pk):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()

    invoice = Invoice.objects.get(id=pk)
    invoice_detail = InvoiceDetail.objects.get(id=pk)

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
        'total_invoice': total_invoice,

        'invoice': invoice,
        'invoice_detail': invoice_detail,
    }

    return render(request, 'invoice/view_invoice_detail.html', context)
