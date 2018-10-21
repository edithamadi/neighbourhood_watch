from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length = 100)
    location = [
        ('Nairobi', 'Nairobi'),
        ('Kisumu', 'Kisumu'),
        ('Mombasa', 'Mombasa'),
        ('Eldoret', 'Eldoret'),
    ]
    local  = models.CharField(max_length=100, choices=location)
    occupants = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Business(models.Model):
    name = models.CharField(max_length = 100)
    user = models.ForeignKey(User)
    hood = models.ForeignKey(Neighbourhood,blank=True)
    email = models.CharField(max_length=150)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=200)
    profile_photo = models.ImageField(upload_to='profile/')
    hood = models.ForeignKey(Neighbourhood, blank=True, null=True)

class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=350)
    hood = models.ForeignKey(Neighbourhood, blank=True,on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)

class Comment(models.Model):
    comments = models.CharField(max_length = 500)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)

