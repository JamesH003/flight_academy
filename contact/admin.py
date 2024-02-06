from django.contrib import admin
from django.db import models
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("msg_date", "first_name", "last_name", "email", "phone_num", "specific_course", "message",)
    list_filter = ("email", )
    search_fields = ["email", "last_name"]