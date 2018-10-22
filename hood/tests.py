from django.test import TestCase
from .models import Neighbourhood,Business
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
        
    def test_save_hood(self):

        self.Nairobi.save_hood()
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods) > 0)

    def test_delete_hood(self):

        self.Nairobi.save_hood()
        self.Nairobi.delete_hood()

    def test_update_hood(self):
    
        new_hood = Neighbourhood.objects.filter(name='nyati').update(name='mbuzi')
        hoods = Neighbourhood.objects.get(name='mbuzi')
        self.assertTrue(hoods.name, 'mbuzi')

class BusinessTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create(id =1, username='b')
        self.Nairobi = Neighbourhood(name='nyati', locale='Nairobi', user=self.user, occupants=5)
        self.Nairobi.save_hood()
        self.biz = Business(name="biznaa", email="adriel@gmail.com", user=self.user, hood=self.Nairobi)

    def test_instance(self):
        self.assertTrue(isinstance(self.biz,Business))

    def test_save_business(self):

        self.biz.save_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_business(self):

        self.biz.save_business()
        self.biz.delete_business()


    
        