from django.db import models
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField


class Nomspot(TimeStampedModel):
    class Goodness(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        TERRIBLE = "terrible", "Terrible"
        OK = "ok", "Ok"
        GOOD = "good", "Good"

    name = models.CharField("Name of food place", max_length=255)
    slug = AutoSlugField("Nomspot address",
        unique=True,    always_update=False, populate_from="name")
    description = models.TextField("Description", blank=True)
    goodness = models.CharField("How good the place is", max_length=20,
        choices=Goodness.choices, default=Goodness.UNSPECIFIED)
    def __str__(self):
        return self.name



