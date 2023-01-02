# Generated by Django 4.1.4 on 2023-01-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claritymedapp', '0004_navclass_name_class'),
    ]

    operations = [
        migrations.CreateModel(
            name='clients1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_client', models.CharField(max_length=50, null=True, verbose_name='שם מטופל')),
                ('id_c', models.CharField(max_length=10, null=True, verbose_name='תז מטופל')),
                ('phone', models.CharField(max_length=10, null=True, verbose_name='מספר טלפון')),
                ('status', models.CharField(max_length=50, null=True, verbose_name='סטטוס מטופל')),
                ('class_c', models.CharField(max_length=50, null=True, verbose_name='מחלקה')),
            ],
        ),
    ]