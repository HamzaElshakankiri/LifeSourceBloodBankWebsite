# Generated by Django 2.2.3 on 2023-03-13 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0009_events_event_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_type',
            field=models.CharField(default='', max_length=25),
        ),
    ]
