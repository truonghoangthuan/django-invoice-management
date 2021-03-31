from django.db import models


# Create your models here.
class Product(models.Model):
    # product_id = models.CharField(max_length=10)
    product_name = models.CharField(max_length=255)
    product_price = models.FloatField()
    product_unit = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('others', 'Others'),
    )
    # customer_id = models.CharField(max_length=10)
    customer_name = models.CharField(max_length=255)
    customer_gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    customer_dob = models.DateField()
    customer_points = models.IntegerField()

    def __str__(self):
        return str(self.id)

class InvoiceDetail(models.Model):
    # invoice_detail_id = models.CharField(max_length=10)
    invoice_detail_product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    invoice_detail_product_amount = models.IntegerField()

    def __str__(self):
        return str(self.id)

class Invoice(models.Model):
    invoice_id = models.ForeignKey(InvoiceDetail, on_delete=models.CASCADE)
    invoice_date = models.DateField(auto_now_add=True)
    invoice_total = models.FloatField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.invoice_id.id)
