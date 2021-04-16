from django.forms import inlineformset_factory, formset_factory
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

    form = InvoiceForm()
    formset = InvoiceDetailFormSet()
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        formset = InvoiceDetailFormSet(request.POST)
        if form.is_valid():
            invoice = Invoice.objects.create(customer=form.cleaned_data.get('customer'),
                                             date=form.cleaned_data.get('date'))
        if formset.is_valid():
            total = 0
            for form in formset:
                product = form.cleaned_data.get('product')
                amount = form.cleaned_data.get('amount')
                if product and amount:
                    # Sum each row
                    sum = float(product.product_price) * float(amount)
                    # Sum of total invoice
                    total += sum
                    InvoiceDetail(invoice=invoice,
                                  product=product,
                                  amount=amount).save()
            # Pointing the customer
            points = 0
            if total > 1000:
                points += total / 1000
            invoice.customer.customer_points = round(points)
            # Save the points to Customer table
            invoice.customer.save()

            # Save the invoice
            invoice.total = total
            invoice.save()
            return redirect('view_invoice')

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
        'total_invoice': total_invoice,

        'form': form,
        'formset': formset,
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


# Detail view of invoices
def view_invoice_detail(request, pk):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()

    invoice = Invoice.objects.get(id=pk)
    invoice_detail = InvoiceDetail.objects.filter(invoice=invoice)

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
        'total_invoice': total_invoice,

        # 'invoice': invoice,
        'invoice_detail': invoice_detail,
    }

    return render(request, 'invoice/view_invoice_detail.html', context)


# Delete invoice
def delete_invoice(request, pk):
    total_product = Product.objects.count()
    total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()

    invoice = Invoice.objects.get(id=pk)
    invoice_detail = InvoiceDetail.objects.filter(invoice=invoice)
    if request.method == 'POST':
        invoice_detail.delete()
        invoice.delete()
        return redirect('view_invoice')

    context = {
        'total_product': total_product,
        'total_customer': total_customer,
        'total_invoice': total_invoice,

        'invoice': invoice,
        'invoice_detail': invoice_detail,
    }

    return render(request, 'invoice/delete_invoice.html', context)
