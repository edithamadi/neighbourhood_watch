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
    local  = models.CharField(max_length=00, choices=location)
    occupants = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
