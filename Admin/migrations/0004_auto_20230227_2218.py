# Generated by Django 2.2.3 on 2023-02-28 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_events'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AlterField(
            model_name='events',
            name='edate',
            field=models.DateField(default='DD-MM-YYYY'),
        ),
    ]