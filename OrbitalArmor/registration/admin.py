from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import RegistrationForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = RegistrationForm
    model = CustomUser

admin.site.register(CustomUser)
