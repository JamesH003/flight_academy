from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.training, name='training'),
    path('add_training/', views.add_training, name='add_training'),
    path('<training_id>/', views.training_detail, name='training_detail'),
]
