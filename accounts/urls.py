from django.urls import path
from . import views

urlpatterns = [
    path('', views.choose_role, name='choose'),
    path('customer/register/', views.customer_register, name='customer_register'),
    path('vendor/register/', views.vendor_register, name='vendor_register'),
    path('delivery/register/', views.delivery_register, name='delivery_register'),
]

