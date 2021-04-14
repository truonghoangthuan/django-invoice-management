from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    
    path('create_product/', views.create_product, name='create_product'),
    path('view_product/', views.view_product, name='view_product'),

    path('create_customer/', views.create_customer, name='create_customer'),
    path('view_customer/', views.view_customer, name='view_customer'),

    path('create_invoice/', views.create_invoice, name='create_invoice'),
    path('view_invoice/', views.view_invoice, name='view_invoice'),

    path('create_invoice_detail/', views.create_invoice_detail, name='create_invoice_detail'),
    path('view_invoice_detail/<int:pk>/', views.view_invoice_detail, name='view_invoice_detail'),

    path('delete_invoice/', views.delete_invoice, name='delete_invoice'),
]
