# Generated by Django 3.0.5 on 2023-03-07 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_postal', models.CharField(max_length=10)),
                ('donor_bio_sex', models.CharField(max_length=25)),
                ('donor_blood_type', models.CharField(max_length=10)),
                ('donor_birthday', models.DateField(null=True)),
                ('donor_weight', models.PositiveIntegerField(default=0)),
                ('donor_height', models.PositiveIntegerField(default=0)),
                ('donor_contact_phone', models.CharField(max_length=25)),
                ('emergency_contact_name', models.CharField(max_length=25)),
                ('emergency_contact_phone', models.CharField(max_length=25)),
                ('donor_nextdonationdate', models.DateField(auto_now=True)),
                ('donor_email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
