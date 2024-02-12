from django import forms
from .models import Training, Licence


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = [
            'title', 'description', 'licence_type', 'cost',
            'mode_of_training', 'aircraft_type', 'image'
        ]

    def __init__(self, *args, **kwargs):
        # https://stackoverflow.com/a/72025478
        super().__init__(*args, **kwargs)
