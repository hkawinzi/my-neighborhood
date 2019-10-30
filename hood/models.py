from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)
    user_id = models.IntegerField()
    hood_id = models.IntegerField(blank=True, null=True)
    email = models.EmailField()
    date = models.DateField()
    location = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='picture/', blank=True)
    contact_info = models.CharField(max_length=300, blank=True)


class Neighbourhood(models.Model):
    name = models.CharField(max_length=70)
    location = models.ManyToManyField(User)
    occupants_count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

    def delete_neighbourhood(self):
        self.delete()

    def update_location(self, location):
        self.location = location
        self.save()

    def update_occupants_count(self, occupants_count):
        self.occupants_count = occupants_count
        self.save()


class Business(models.Model):
    name = models.CharField(max_length=100)
    email_address = models.TextField()
    user = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def delete_business(self):
        self.delete()

    def update_business(self, business):
        self.update_business()
        self.save()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='picture/', blank=True)
    bio = models.TextField(default='')
    posted_project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)
    contact_info = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self, bio):
        self.bio = bio
        self.save()

