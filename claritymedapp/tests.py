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
    
    def count_user(self):
        user_count = User.objects.count()
        self.assertTrue(user_count==1)


class clientTestCase(TestCase):
    def setUp(self):
        clients1.objects.create(name_client='TOMER',id_c='207338351',phone='0547407404',status='IN PROG',class_c='General')

    def test_user_created(self):
        client=clients1.objects.filter(name_client='TOMER',id_c='207338351',phone='0547407404',status='IN PROG',class_c='General')
        self.assertTrue(client.exists())
        
    def count_clients(self):
        user_count = clients1.objects.count()
        self.assertTrue(user_count==1)



class SurveyFormTestCase(TestCase):
    def setUp(self):
        survey.objects.create(cleaning='טוב',security='רע',treatment='טוב',facilities='רע',food='טוב')

    def test_survey_created(self):
        survey1=survey.objects.filter(cleaning='טוב',security='רע',treatment='טוב',facilities='רע',food='טוב')
        self.assertTrue(survey1.exists())

class NavClassTestCase(TestCase):
    def setUp(self):
        NavClass.objects.create(name_class='GENERAL',navs='BUILDING A')

    def test_NavClass_created(self):
        nav1=NavClass.objects.filter(name_class='GENERAL',navs='BUILDING A')
        self.assertTrue(nav1.exists())

class doc_appTestCase(TestCase):
    def setUp(self):
        doc_app.objects.create(doc_id='204551236',doc_name='Avi',client_id='341552415',client_name='Tomer',date_app='2022-04-02')

    def test_app_created(self):
        app=doc_app.objects.filter(doc_id='204551236',doc_name='Avi',client_id='341552415',client_name='Tomer',date_app='2022-04-02')
        self.assertTrue(app.exists())
