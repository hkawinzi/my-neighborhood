from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    user_id = models.AutoField()
    hood_id = models.IntegerField()
    email = models.TextField()
    date = models.DateField()
    location = models.OneToOneField(User, on_delete=models.CASCADE)


class Neighbourhood(models.Model):
    name = models.CharField(max_length=70)
    location = models.ManyToManyField(User)
    occupants_count = models.IntegerField()


class Business(models.Model):
    name = models.CharField(max_length=100)
    email_address = models.TextField()
    user = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
