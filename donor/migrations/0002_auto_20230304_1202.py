# Generated by Django 3.0.5 on 2023-03-04 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donor',
            old_name='donor_password',
            new_name='donor_pass',
        ),
    ]