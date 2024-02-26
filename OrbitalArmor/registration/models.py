from django.db import models
from django.forms import ModelForm
from django_countries.fields import CountryField
from django_countries import countries
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(unique=True, blank=False, null=False)
    town = models.CharField(blank=False, max_length=50, name='town', error_messages='Please enter town data...')
    company = models.CharField(blank=False, max_length=50, name='company', error_messages="Company name required...")
    position = models.CharField(blank=False,max_length=50, name='position', error_messages="Position in company is required...")
    country = models.CharField(max_length=200,  null=True, choices=CountryField().choices + [('', 'Select Country')] , blank=False)
    terms = models.BooleanField(blank=False, error_messages="Must read terms and conditions to continue...")
    