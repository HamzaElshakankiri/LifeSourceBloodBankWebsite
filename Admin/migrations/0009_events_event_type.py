# Generated by Django 2.2.3 on 2023-03-13 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0008_auto_20230312_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_type',
            field=models.CharField(default='Unknown', max_length=25),
        ),
    ]