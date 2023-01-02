from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User
from django.test import TestCase
from .models import survey,doc_app,NavClass,clients1

class AuthenticationTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='testu', email='testu@gmail.com',password='ATOato123')

    def test_user_created(self):
        user=User.objects.filter(username='testu', email='testu@gmail.com',password='ATOato123')
        self.assertTrue(user.exists())
    
    def test_no_user_found(self):
        user=User.objects.filter(username='test1', email='test1@gmail.com')
        self.assertFalse(user.exists())


class clientTestCase(TestCase):
    def setUp(self):
        clients1.objects.create(name_client='TOMER',id_c='207338351',phone='0547407404',status='IN PROG',class_c='General')

    def test_user_created(self):
        client=clients1.objects.filter(name_client='TOMER',id_c='207338351',phone='0547407404',status='IN PROG',class_c='General')
        self.assertTrue(client.exists())
