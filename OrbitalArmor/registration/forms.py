from django import forms
from django.forms import ModelForm
from .models import CustomUser
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        widgets = { 'country': CountrySelectWidget}
        fields = ['username','first_name', 'last_name', 'email', 'phone_number', 'password1', 'town', 'company', 'position', 'terms']

        def cleanData(self):
            cleaned_data = super(RegistrationForm,self).clean()
            password = cleaned_data.get('password1')
            password_confirm = cleaned_data.get('password2')
            
            if password and password_confirm:
                if password != password_confirm:
                    raise forms.ValidationError("The two passwords fields must match")
            
            return cleaned_data