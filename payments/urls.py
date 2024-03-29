from django.contrib import admin
from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.payments, name='payments'),
    path(
        'payments_success/<order_number>', views.payments_success,
        name='payments_success'),
    path(
        'cache_checkout_data/', views.cache_checkout_data,
        name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
