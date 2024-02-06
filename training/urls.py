from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.training, name='training'),
    path('<training_id>/', views.training_detail, name='training_detail'),
]
