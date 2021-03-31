from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create_product/', views.create_product, name='create_product'),
    path('view_product/', views.view_product, name='view_product'),
    path('create_customer/', views.create_customer, name='create_customer'),
    path('view_customer/', views.view_customer, name='view_customer'),
]