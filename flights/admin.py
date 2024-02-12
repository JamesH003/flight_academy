from django.contrib import admin
from .models import Aircraft, Voucher


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
        'aircraft_type',
        'duration',
        'cost',
        'image',
    )

    ordering = ('title',)


admin.site.register(Aircraft, AircraftAdmin)
admin.site.register(Voucher, VoucherAdmin)
