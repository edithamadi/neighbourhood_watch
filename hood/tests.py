from django.test import TestCase
from .models import Neighbourhood,Business,Profile,Post,Comment,category,Location
from django.contrib.auth.models import User
# Create your tests here.

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.new_user = User(username='adriel',email='adriel@gmail.com')
        self.new_user.save()
        self.Nairobi = Neighbourhood(locale='nyati',location='Nairobi',occupants=5)
        self.Nairobi.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.Nairobi,Neighbourhood))
        
