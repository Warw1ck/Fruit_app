from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


class FruitModel(models.Model):
    name = models.CharField(max_length=30,
                            validators=[MinLengthValidator(2, "Fruit name should contain only letters!")]
                            )
    image_url = models.URLField()
    description = models.TextField()
    nutrients = models.TextField(null=True, blank=True)