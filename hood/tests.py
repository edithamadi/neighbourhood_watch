from django.test import TestCase
from .models import Neighbourhood
from django.contrib.auth.models import User
# Create your tests here.

class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.new_user = User(id='1', username='adriel',email='adriel@gmail.com')
        self.new_user.save()
        self.Nairobi = Neighbourhood(name='nyati',locale='Nairobi',occupants=5, user=self.new_user)
        self.Nairobi.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.Nairobi,Neighbourhood))
        
    def test_save_method(self):

        self.Nairobi.save_hood()
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods) > 0)

    def test_delete_method(self):

        self.Nairobi.save_hood()
        self.Nairobi.delete_hood

    

    

    


