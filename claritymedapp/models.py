from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class survey(models.Model):
    cleaning= models.CharField('Cleaning',max_length=20)
    security= models.CharField('Security',max_length=20)
    treatment= models.CharField('Treatment',max_length=20)
    facilities= models.CharField('Facilities',max_length=20)
    food= models.CharField('Food',max_length=20)
    

    
