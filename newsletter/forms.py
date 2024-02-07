from django import forms
from .models import Newsletter


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = [
            'email'
        ]

    def __init__(self, *args, **kwargs):
        # https://stackoverflow.com/a/72025478
        super().__init__(*args, **kwargs)
