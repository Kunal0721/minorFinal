# Generated by Django 5.0.1 on 2024-02-10 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_registration_gender_remove_registration_state_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='lo',
        ),
        migrations.DeleteModel(
            name='registration',
        ),
    ]