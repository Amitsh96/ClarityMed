
# Generated by Django 4.1.3 on 2022-12-15 21:59

# Generated by Django 4.1.4 on 2022-12-15 21:59


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cleaning', models.CharField(max_length=20, verbose_name='Cleaning')),
                ('security', models.CharField(max_length=20, verbose_name='Security')),
                ('treatment', models.CharField(max_length=20, verbose_name='Treatment')),
                ('facilities', models.CharField(max_length=20, verbose_name='Facilities')),
                ('food', models.CharField(max_length=20, verbose_name='Food')),
            ],
        ),
    ]