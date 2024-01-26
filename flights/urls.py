from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_vouchers, name='vouchers'),
    path('add_voucher/', views.add_voucher, name='add_voucher'),
    path('<voucher_id>/', views.voucher_detail, name='voucher_detail'),
]
