from django.contrib import admin
from .models import User, Profile, Neighbourhood, Business

# Register your models here.
admin.register(User)
admin.register(Profile)
admin.register(Neighbourhood)
admin.register(Business)
