from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length = 100)
    location = (
        ('Nairobi', 'Nairobi'),
        ('Kisumu', 'Kisumu'),
        ('Mombasa', 'Mombasa'),
        ('Eldoret', 'Eldoret'),
    )
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
    def update_occupants(cls, id):
        hoods = cls.objects.filter(id=id).update_occupants(id=id)
        return hoods

class Business(models.Model):
    name = models.CharField(max_length = 100)
    user = models.ForeignKey(User)
    hood = models.ForeignKey(Neighbourhood,blank=True)
    email = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.name}"

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_businesses(cls, search_term):
        businesses = cls.objects.filter(business_name__icontains=search_term)
        return businesses

    @classmethod
    def find_businesses(cls, id):
        businesses = cls.objects.filter(id=id).find(id=id)
        return businesses

    @classmethod
    def update_businesses(cls, id):
        businesses = cls.objects.filter(id=id).update(id=id)
        return businesses

    @classmethod
    def add_businesses(cls, id):
        businesses = cls.objects.filter(id=id).add(id=id)
        return businesses


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

    def __str__(self):
        return self.description

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def create_post(cls, id):
        hoods = cls.objects.filter(id=id).create(id=id)
        return posts

class Comment(models.Model):
    comments = models.CharField(max_length = 500)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    def __str__(self):
        return self.comments

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    