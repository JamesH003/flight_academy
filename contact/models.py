from django.db import models
from training.models import Training


class Contact(models.Model):
    """ A model to handle a contact form """

    first_name = models.CharField(max_length=75, blank=False, null=False)
    last_name = models.CharField(max_length=75, blank=False, null=False)
    email = models.EmailField(max_length=256, blank=False, null=False)
    phone_num = models.CharField(max_length=30, null=True)
    specific_course = models.ForeignKey(
        Training, on_delete=models.CASCADE, null=False, blank=False)
    message = models.TextField(blank=False, null=False)
    msg_date = models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self):
        return self.email


