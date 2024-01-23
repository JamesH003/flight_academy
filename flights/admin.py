from django.contrib import admin
from .models import Aircraft, Voucher

# Register your models here.

class AircraftAdmin(admin.ModelAdmin):
    list_display = (
        'aircraft_type',
        'seats',
        'engines',
    )

    ordering = ('aircraft_type',)

class VoucherAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'duration',
        'cost',
        'image',
    )

    ordering = ('title',)

admin.site.register(Aircraft, AircraftAdmin)
admin.site.register(Voucher, VoucherAdmin)