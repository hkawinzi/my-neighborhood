from django.test import TestCase
from django.test import TestCase
from .models import Neighbourhood, Profile, Business
from django.contrib.auth.models import User
# Create your tests here.


class Neighbourhood_TestCases(TestCase):
    def setUp(self):
       self.user1= User(id=1,username='happy', email='happy@gmail.com', password='1234')
       self.user1.save()
       self.profile = Profile(user_id=1, bio='i love smiling', profile_pic='images/default.jpg')
       self.profile.save_profile()
       self.neighborhood =Neighbourhood(id=1,name='nairobi', health_department_address='99300', health='mUK', count='4')
       self.neighborhood.create_neighborhood()
       self.business = Business(id=1, business_name = 'coding', business_email='m@gmail.com')


    def tearDown(self):
       Profile.objects.all().delete()
       User.objects.all().delete()
       Neighbourhood.objects.all().delete()

    def test_is_instance(self):
       self.assertTrue(isinstance(self.user1, User))
       self.assertTrue(isinstance(self.profile, Profile))
       self.assertTrue(isinstance(self.neighborhood, Neighbourhood))

    def test_save_method(self):
       self.neighborhood.create_neighbourhood()
       all_objects = Neighbourhood.objects.all()
       self.assertTrue(len(all_objects)>0)

   def test_delete_method(self):
       self.neighborhood.create_neighborhood()
       filtered_object = Neighbourhood.objects.filter(name='nairobi')
       filtered_object.delete()
       all_objects = Neighbourhood.objects.all()
       self.assertTrue(len(all_objects) == 0)

   def test_display_all_objects_method(self):
       self.neighborhood.create_neighborhood()
       all_objects = Neighbourhood.retrieve_all()
       self.assertEqual(all_objects.name,'nairobi')

   def test_update_single_object_property(self):
       self.neighborhood.create_neighborhood()
       filtered_object =Neighbourhood.update_occupants('4','5')
       fetched = Neighbourhood.objects.get(count='5')
       self.assertEqual(fetched.count,'5')

   def test_find_neighborhood_by_id(self):
       self.neighborhood.create_neighborhood()
       fetched_neighborhood = Neighbourhood.find_neighborhood_by_id(1)
       self.assertEqual(fetched_neighborhood.id,1)
