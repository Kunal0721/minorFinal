# Generated by Django 5.0.1 on 2024-03-17 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_beds_patient_info_bed_id_patient_info_bed_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient_info',
            name='Emargency_number',
        ),
    ]