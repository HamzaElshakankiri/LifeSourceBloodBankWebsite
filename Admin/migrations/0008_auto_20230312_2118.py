# Generated by Django 2.2.3 on 2023-03-13 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0007_auto_20230312_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='apptname',
        ),
        migrations.RemoveField(
            model_name='events',
            name='elocation',
        ),
    ]
