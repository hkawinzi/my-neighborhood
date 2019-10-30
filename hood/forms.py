from django import forms
from .models import Neighbourhood, Business, Profile, Post


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('image', 'contact_info')


class NewHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ('name', 'location')


class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ('name', 'email_address')


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['owner','post_date','hood','profile']

