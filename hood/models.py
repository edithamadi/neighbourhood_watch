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
    locale  = models.CharField(max_length=100, choices=location)
    occupants = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.locale}"

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    @classmethod
    def search_hood(cls , search_term):
        hoods = cls.objects.filter( name__icontains = search_term ) 
        return hoods

    @classmethod
    def create_hood(cls, id):
        hoods = cls.objects.filter(id=id).create(id=id)
        return hoods

    @classmethod
    def find_hood(cls, id):
        hoods = cls.objects.filter(id=id).find(id=id)
        return hoods

    @classmethod
    def update_hood(cls, id):
        hoods = cls.objects.filter(id=id).update(id=id)
        return hoods

    @classmethod
    def update_occupants(cls, id):
        hoods = cls.objects.filter(id=id).update_occupants(id=id)
        return hoods




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

