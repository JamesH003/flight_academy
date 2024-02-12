from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField
from django.db import models

from flights.models import Aircraft


class Licence(models.Model):
    """
    A model to handle licence types
    """
    ENGINES = [("1", "1"), ("2", "2"), ]

    licence_type = models.CharField(max_length=100, null=False, blank=False)
    required_flight_time = models.PositiveIntegerField(
        default=30,
        validators=[MinValueValidator(30), MaxValueValidator(1500)],
        null=False, blank=False
    )
    engines = models.CharField(
        choices=ENGINES, default="1",
        max_length=1, null=False, blank=False)

    class Meta:
        ordering = ["required_flight_time"]

    def __str__(self):
        return self.licence_type


class Training(models.Model):
    """
    A model to handle the training course options
    """
    MODES = [
        ("Modular", "Modular"),
        ("Integrated", "Integrated"),
    ]

    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    licence_type = models.ForeignKey(
        Licence, on_delete=models.CASCADE, null=False, blank=False)
    cost = models.PositiveIntegerField(null=False, blank=False)
    mode_of_training = models.CharField(
        choices=MODES, default="Modular", max_length=50,
        null=False, blank=False
    )
    aircraft_type = models.ForeignKey(
        Aircraft, on_delete=models.CASCADE, null=False, blank=False)
    image = CloudinaryField(
        "image", default="placeholder", null=False, blank=False)

    class Meta:
        ordering = ["cost"]
        verbose_name_plural = 'Training'

    def __str__(self):
        return self.title
