from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class clients1(models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    name_client=models.CharField('שם מטופל',null=True,max_length=50)
    id_c=models.CharField('תז מטופל',null=True,max_length=10)
    phone=models.CharField('מספר טלפון',null=True,max_length=10)
    status=models.CharField('סטטוס מטופל',null=True,max_length=50)
    class_c=models.CharField('מחלקה',null=True,max_length=50)

    def __str__(self):
        return self.name_client

class NavClass(models.Model):
    name_class=models.CharField('class name',null=True,max_length=50)
    navs = models.TextField()

    def __str__(self):
        return self.name_class

class survey(models.Model):
    cleaning= models.CharField('רמת נקיון בבית החולים',max_length=20)
    security= models.CharField('רמת האבטחה בבית החולים',max_length=20)
    treatment= models.CharField('הטיפול הרפואי שקיבלת',max_length=20)
    facilities= models.CharField('תחזוקת המקום (שירותים, גינון וכולי)',max_length=20)
    food= models.CharField('רמת האוכל המוגש בבית החולים',max_length=20)
    

class doc_app(models.Model):
    doc_id= models.CharField('מספר רופא',max_length=50)
    doc_name= models.CharField('שם רופא',max_length=50)
    client_id= models.CharField('תז מטופל',max_length=50)
    client_name= models.CharField('שם מטופל',max_length=50)
    date_app= models.DateField('תאריך טיפול')
    

class recep_eq(models.Model):
    name_eq=models.CharField('שם המוצר',null=True,max_length=50)
    price = models.CharField('מחיר',null=True,max_length=50)
    des=models.TextField()


    def __str__(self):
        return self.name_eq
    



class order_recep(models.Model):
     qunt1=models.IntegerField(' כמות חבילת עטים להזמנה ',null=True)
     qunt2=models.IntegerField(' כמות קלסר משרדי להזמנה ',null=True)
     qunt3=models.IntegerField(' כמות סיכות לשדכן להזמנה ',null=True)
     qunt4=models.IntegerField(' כמות תיקי הגשה להזמנה ',null=True)
     qunt5=models.IntegerField(' כמות שדכן סיכות להזמנה ',null=True)
     qunt6=models.IntegerField(' כמות מטליות חיטוי להזמנה ',null=True)
     qunt7=models.IntegerField(' כמות דיו מדפסת להזמנה ',null=True)
     qunt8=models.IntegerField(' כמות נייר מדפסת להזמנה ',null=True)

    

class doc_eq(models.Model):
    name_eq=models.CharField('שם המוצר',null=True,max_length=50)
    price = models.CharField('מחיר',null=True,max_length=50)
    des=models.TextField()


    def __str__(self):
        return self.name_eq
    



class order_doc(models.Model):
     qunt1=models.IntegerField(' כמות כפפות להזמנה ',null=True)
     qunt2=models.IntegerField(' כמות מסכות להזמנה ',null=True)
     qunt3=models.IntegerField(' כמות חלוק רפואי להזמנה ',null=True)
     qunt4=models.IntegerField(' כמות מזרקים להזמנה ',null=True)
     qunt5=models.IntegerField(' כמות תחבושות להזמנה ',null=True)
     qunt6=models.IntegerField(' כמות חומר חיטוי להזמנה ',null=True)
     qunt7=models.IntegerField(' כמות פד גזה להזמנה ',null=True)
     qunt8=models.IntegerField(' כמות מבחנות להזמנה ',null=True)

    