from django.db import models


# Create your models here.
class Product(models.Model):
    # product_id = models.CharField(max_length=10)
    product_name = models.CharField(max_length=255)
    product_price = models.FloatField()
    product_unit = models.CharField(max_length=255)

    def __str__(self):
        return str(self.product_name)


class Customer(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    # customer_id = models.CharField(max_length=10)
    customer_name = models.CharField(max_length=255)
    customer_gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    customer_dob = models.DateField()
    customer_points = models.IntegerField()

    def __str__(self):
        return str(self.customer_name)

class InvoiceDetail(models.Model):
    # invoice_detail_id = models.CharField(max_length=10)
    invoice_detail_product_name = models.ForeignKey(Product, on_delete=models.CASCADE)
    invoice_detail_product_amount = models.IntegerField()

    def __str__(self):
        return str(self.id)

class Invoice(models.Model):
    # invoice_id = models.CharField(max_length=10)
    # id = models.ForeignKey(InvoiceDetail, on_delete=models.CASCADE)
    invoice_detail = models.ForeignKey(InvoiceDetail, on_delete=models.CASCADE)
    invoice_date = models.DateField()
    invoice_total = models.FloatField()
    invoice_customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.invoice_detail.id)

    def get_total_bill(self):
        amount = self.invoice_detail.invoice_detail_product_amount
        product_price = invoice_detail.invoice_detail_product_amount.product_price

        invoice_total = amount * product_price

        return invoice_total
