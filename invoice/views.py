from django.http import HttpResponse
from django.shortcuts import render, redirect

from utils.filehandler import handle_file_upload

from .forms import *
from .models import *
import pandas as pd

# Create your views here.


def getTotalIncome():
    allInvoice = Invoice.objects.all()
    totalIncome = 0
    for curr in allInvoice:
        totalIncome += curr.total
    return totalIncome


def base(request):
    total_product = Product.objects.count()
    # total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()
    total_income = getTotalIncome()
    context = {
        "total_product": total_product,
        # "total_customer": total_customer,
        "total_invoice": total_invoice,
        "total_income": total_income,
    }

    return render(request, "invoice/base/base.html", context)


def download_all(request):
    # Download all invoice to excel file
    # Download all product to excel file
    # Download all customer to excel file

    allInvoiceDetails = InvoiceDetail.objects.all()
    invoiceAndProduct = {
        "invoice_id": [],
        "invoice_date": [],
        "invoice_customer": [],
        "invoice_contact": [],
        "invoice_email": [],
        "invoice_comments": [],
        "product_name": [],
        "product_price": [],
        "product_unit": [],
        "product_amount": [],
        "invoice_total": [],

    }
    for curr in allInvoiceDetails:
        invoice = Invoice.objects.get(id=curr.invoice_id)
        product = Product.objects.get(id=curr.product_id)
        invoiceAndProduct["invoice_id"].append(invoice.id)
        invoiceAndProduct["invoice_date"].append(invoice.date)
        invoiceAndProduct["invoice_customer"].append(invoice.customer)
        invoiceAndProduct["invoice_contact"].append(invoice.contact)
        invoiceAndProduct["invoice_email"].append(invoice.email)
        invoiceAndProduct["invoice_comments"].append(invoice.comments)
        invoiceAndProduct["product_name"].append(product.product_name)
        invoiceAndProduct["product_price"].append(product.product_price)
        invoiceAndProduct["product_unit"].append(product.product_unit)
        invoiceAndProduct["product_amount"].append(curr.amount)
        invoiceAndProduct["invoice_total"].append(invoice.total)

    df = pd.DataFrame(invoiceAndProduct)
    df.to_excel("static/excel/allInvoices.xlsx", index=False)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="allInvoices.xlsx"'
    with open("static/excel/allInvoices.xlsx", "rb") as f:
        response.write(f.read())
    return response


def delete_all_invoice(request):
    # Delete all invoice
    Invoice.objects.all().delete()
    return redirect("view_invoice")


def upload_product_from_excel(request):
    # Upload excel file to static folder "excel"
    # add all product to database
    # save product to database
    # redirect to view_product
    excelForm = excelUploadForm(request.POST or None, request.FILES or None)
    print("Reached HERE!")
    if request.method == "POST":
        print("Reached HERE2222!")

        handle_file_upload(request.FILES["excel_file"])
        excel_file = "static/excel/masterfile.xlsx"
        df = pd.read_excel(excel_file)
        Product.objects.all().delete()
        for index, row in df.iterrows():
            product = Product(
                product_name=row["product_name"],
                product_price=row["product_price"],
                product_unit=row["product_unit"],
            )
            print(product)
            product.save()
        return redirect("view_product")
    return render(request, "invoice/upload_products.html", {"excelForm": excelForm})

    # Product view


def create_product(request):
    total_product = Product.objects.count()
    # total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()
    total_income = getTotalIncome()

    product = ProductForm()

    if request.method == "POST":
        product = ProductForm(request.POST)
        if product.is_valid():
            product.save()
            return redirect("create_product")

    context = {
        "total_product": total_product,
        # "total_customer": total_customer,
        "total_invoice": total_invoice,
        "total_income": total_income,
        "product": product,
    }

    return render(request, "invoice/create_product.html", context)


def view_product(request):
    total_product = Product.objects.count()
    # total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()
    total_income = getTotalIncome()

    product = Product.objects.filter(product_is_delete=False)
    print(product)
    context = {
        "total_product": total_product,
        # "total_customer": total_customer,
        "total_invoice": total_invoice,
        "total_income": total_income,
        "product": product,
    }

    return render(request, "invoice/view_product.html", context)


# Customer view
# def create_customer(request):
#     total_product = Product.objects.count()
#     total_customer = Customer.objects.count()
#     total_invoice = Invoice.objects.count()

#     customer = CustomerForm()

#     if request.method == "POST":
#         customer = CustomerForm(request.POST)
#         if customer.is_valid():
#             customer.save()
#             return redirect("create_customer")

#     context = {
#         "total_product": total_product,
#         "total_customer": total_customer,
#         "total_invoice": total_invoice,
#         "customer": customer,
#     }

#     return render(request, "invoice/create_customer.html", context)


# def view_customer(request):
#     total_product = Product.objects.count()
#     total_customer = Customer.objects.count()
#     total_invoice = Invoice.objects.count()

#     customer = Customer.objects.all()

#     context = {
#         "total_product": total_product,
#         "total_customer": total_customer,
#         "total_invoice": total_invoice,
#         "customer": customer,
#     }

#     return render(request, "invoice/view_customer.html", context)


# Invoice view
def create_invoice(request):
    total_product = Product.objects.count()
    # total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()
    total_income = getTotalIncome()

    form = InvoiceForm()
    formset = InvoiceDetailFormSet()
    if request.method == "POST":
        form = InvoiceForm(request.POST)
        formset = InvoiceDetailFormSet(request.POST)
        if form.is_valid():
            invoice = Invoice.objects.create(
                customer=form.cleaned_data.get("customer"),
                contact=form.cleaned_data.get("contact"),
                email=form.cleaned_data.get("email"),
                date=form.cleaned_data.get("date"),
            )
        if formset.is_valid():
            total = 0
            for form in formset:
                product = form.cleaned_data.get("product")
                amount = form.cleaned_data.get("amount")
                if product and amount:
                    # Sum each row
                    sum = float(product.product_price) * float(amount)
                    # Sum of total invoice
                    total += sum
                    InvoiceDetail(
                        invoice=invoice, product=product, amount=amount
                    ).save()
            # Pointing the customer
            # points = 0
            # if total > 1000:
            #     points += total / 1000
            # invoice.customer.customer_points = round(points)
            # # Save the points to Customer table
            # invoice.customer.save()

            # Save the invoice
            invoice.total = total
            invoice.save()
            return redirect("view_invoice")

    context = {
        "total_product": total_product,
        # "total_customer": total_customer,
        "total_invoice": total_invoice,
        "total_income": total_income,
        "form": form,
        "formset": formset,
    }

    return render(request, "invoice/create_invoice.html", context)


def view_invoice(request):
    total_product = Product.objects.count()
    # total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()
    total_income = getTotalIncome()

    invoice = Invoice.objects.all()

    context = {
        "total_product": total_product,
        # "total_customer": total_customer,
        "total_invoice": total_invoice,
        "total_income": total_income,
        "invoice": invoice,
    }

    return render(request, "invoice/view_invoice.html", context)


# Detail view of invoices
def view_invoice_detail(request, pk):
    total_product = Product.objects.count()
    # total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()
    total_income = getTotalIncome()

    invoice = Invoice.objects.get(id=pk)
    invoice_detail = InvoiceDetail.objects.filter(invoice=invoice)

    context = {
        "total_product": total_product,
        # "total_customer": total_customer,
        "total_invoice": total_invoice,
        "total_income": total_income,
        # 'invoice': invoice,
        "invoice_detail": invoice_detail,
    }

    return render(request, "invoice/view_invoice_detail.html", context)


# Delete invoice
def delete_invoice(request, pk):
    total_product = Product.objects.count()
    # total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()
    total_income = getTotalIncome()

    invoice = Invoice.objects.get(id=pk)
    invoice_detail = InvoiceDetail.objects.filter(invoice=invoice)
    if request.method == "POST":
        invoice_detail.delete()
        invoice.delete()
        return redirect("view_invoice")

    context = {
        "total_product": total_product,
        # "total_customer": total_customer,
        "total_invoice": total_invoice,
        "total_income": total_income,
        "invoice": invoice,
        "invoice_detail": invoice_detail,
    }

    return render(request, "invoice/delete_invoice.html", context)


# # Edit customer
# def edit_customer(request, pk):
#     total_product = Product.objects.count()
#     # total_customer = Customer.objects.count()
#     total_invoice = Invoice.objects.count()

#     customer = Customer.objects.get(id=pk)
#     form = CustomerForm(instance=customer)

#     if request.method == "POST":
#         customer = CustomerForm(request.POST, instance=customer)
#         if customer.is_valid():
#             customer.save()
#             return redirect("view_customer")

#     context = {
#         "total_product": total_product,
#         "total_customer": total_customer,
#         "total_invoice": total_invoice,
#         "customer": form,
#     }

#     return render(request, "invoice/create_customer.html", context)


# Delete customer
# def delete_customer(request, pk):
#     total_product = Product.objects.count()
#     total_customer = Customer.objects.count()
#     total_invoice = Invoice.objects.count()

#     customer = Customer.objects.get(id=pk)

#     if request.method == "POST":
#         customer.delete()
#         return redirect("view_customer")

#     context = {
#         "total_product": total_product,
#         "total_customer": total_customer,
#         "total_invoice": total_invoice,
#         "customer": customer,
#     }

#     return render(request, "invoice/delete_customer.html", context)


# Edit product
def edit_product(request, pk):
    total_product = Product.objects.count()
    # total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()
    total_income = getTotalIncome()

    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == "POST":
        # customer = CustomerForm(request.POST, instance=product)

        product.save()
        return redirect("view_product")

    context = {
        "total_product": total_product,
        # "total_customer": total_customer,
        "total_invoice": total_invoice,
        "total_income": total_income,
        "product": form,
    }

    return render(request, "invoice/create_product.html", context)


# Delete product
def delete_product(request, pk):
    total_product = Product.objects.count()
    # total_customer = Customer.objects.count()
    total_invoice = Invoice.objects.count()
    total_income = getTotalIncome()

    product = Product.objects.get(id=pk)

    if request.method == "POST":
        product.product_is_delete = True
        product.save()
        return redirect("view_product")

    context = {
        "total_product": total_product,
        # "total_customer": total_customer,
        "total_invoice": total_invoice,
        "total_income": total_income,
        "product": product,
    }

    return render(request, "invoice/delete_product.html", context)
