# Generated by Django 3.0.5 on 2023-03-07 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='donor_email',
            field=models.CharField(max_length=20),
        ),
    ]
