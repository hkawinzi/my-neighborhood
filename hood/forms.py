from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Neighbourhood, Business, Profile


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'user_id', 'hood_id', 'email', 'location')


class NewHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ('name', 'location')


class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('name', 'email_address')



