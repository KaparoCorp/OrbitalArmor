from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(unique=True, blank=False, null=False)

    