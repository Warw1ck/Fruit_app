from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.


def name_validator(name):
    if not name[0].isalpha():
        raise ValidationError('Your name must start with letter!')
    else:
        return name


class ProfileModel(models.Model):
    first_name = models.CharField(max_length=25, validators=[MinLengthValidator(2), name_validator])
    last_name = models.CharField(max_length=35, validators=[MinLengthValidator(2), name_validator])
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=20)
    image_url = models.URLField(null=True, blank=True)
    age = models.IntegerField(default=18, null=True, blank=True)
