from django.db import models


class Newsletter(models.Model):
    """
    A model to handle the newsletter signups.
    """
    email = models.EmailField(max_length=256, null=False, blank=False)

    def __str__(self):
        return self.email
