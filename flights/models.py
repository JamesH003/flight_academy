from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField
from django.db import models



class Aircraft(models.Model):
    """
    A model to handle aircraft types.
    """
    SEATS = [("2", "2"), ("4", "4"),]
    ENGINES = [("1", "1"), ("2", "2"),]

    aircraft_type = models.CharField(max_length=100, null=False, blank=False)
    seats = models.CharField(
        choices=SEATS, default="2",
        max_length=1, null=False, blank=False)
    engines = models.CharField(
        choices=ENGINES, default="1",
        max_length=1, null=False, blank=False)

    class Meta:
        ordering = ["aircraft_type"]
        verbose_name_plural = 'Aircraft'

    def __str__(self):
        return self.aircraft_type


class Voucher(models.Model):
    """
    A model to handle the various flight vouchers.
    """
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    duration = models.PositiveIntegerField(
        default=30,
        validators=[MinValueValidator(30)],
        null=False, blank=False)
    cost = models.PositiveIntegerField(null=False, blank=False)
    aircraft_type = models.ForeignKey(
        Aircraft, on_delete=models.CASCADE, null=False, blank=False)
    image = CloudinaryField(
        "image", default="placeholder", null=False, blank=False)

    class Meta:
        ordering = ["cost"]

    def __str__(self):
        return self.title