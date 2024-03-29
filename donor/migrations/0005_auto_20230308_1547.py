# Generated by Django 3.0.5 on 2023-03-08 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donor', '0004_donor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='donor_profile', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
