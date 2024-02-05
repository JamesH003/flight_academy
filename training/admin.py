from django.contrib import admin
from .models import Training, Licence


class TrainingAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'licence_type',
        'cost',
        'mode_of_training',
        'aircraft_type',
        'image',
    )

    ordering = ('cost',)


class LicenceAdmin(admin.ModelAdmin):
    list_display = (
        'licence_type',
        'required_flight_time',
        'engines',
    )

    ordering = ('required_flight_time',)


admin.site.register(Training, TrainingAdmin)
admin.site.register(Licence, LicenceAdmin)


