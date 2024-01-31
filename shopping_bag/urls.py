from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_shopping_bag, name='view_shopping_bag'),
    path('add/<voucher_id>', views.add_to_shopping_bag, name='add_to_shopping_bag'),
    path('adjust/<voucher_id>', views.adjust_shopping_bag, name='adjust_shopping_bag'),
    path('remove/<voucher_id>', views.remove_from_shopping_bag, name='remove_from_shopping_bag'),
]
