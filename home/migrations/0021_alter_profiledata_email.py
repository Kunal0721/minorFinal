# Generated by Django 5.0.1 on 2024-03-29 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_profiledata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiledata',
            name='email',
            field=models.CharField(max_length=200),
        ),
    ]