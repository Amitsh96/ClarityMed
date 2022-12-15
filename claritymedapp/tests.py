from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User
from django.test import TestCase

class AuthenticationTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='testu', email='testu@gmail.com',password='ATOato123')

    def test_user_created(self):
        user=User.objects.filter(username='testu', email='testu@gmail.com',password='ATOato123')
        self.assertTrue(user.exists())
    
    def test_no_user_found(self):
        user=User.objects.filter(username='test1', email='test1@gmail.com')
        self.assertFalse(user.exists())

