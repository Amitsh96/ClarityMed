from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class survey(models.Model):
    cleaning= models.CharField('רמת נקיון בבית החולים',max_length=20)
    security= models.CharField('רמת האבטחה בבית החולים',max_length=20)
    treatment= models.CharField('הטיפול הרפואי שקיבלת',max_length=20)
    facilities= models.CharField('תחזוקת המקום (שירותים, גינון וכולי)',max_length=20)
    food= models.CharField('רמת האוכל המוגש בבית החולים',max_length=20)
    

    
