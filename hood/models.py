from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=30)
    user_id = models.AutoField()
    hood_id = models.IntegerField()
    email = models.TextField()
    date = models.DateField()
    location = models.OneToOneField(User, on_delete=models.CASCADE)
