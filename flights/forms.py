from django import forms
from .models import Aircraft, Voucher


class VoucherForm(forms.ModelForm):
    class Meta:
        model = Voucher
        fields = [
            'title', 'description', 'duration', 'cost',
            'aircraft_type', 'image'
        ]

    def __init__(self, *args, **kwargs):
        # https://stackoverflow.com/a/72025478
        super().__init__(*args, **kwargs)
