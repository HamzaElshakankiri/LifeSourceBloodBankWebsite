# Generated by Django 3.0.5 on 2023-03-13 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0007_auto_20230313_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='donor_contact_phone',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='donor',
            name='emergency_contact_phone',
            field=models.PositiveIntegerField(),
        ),
    ]
