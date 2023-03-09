from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models


class DonorUserForm(forms.ModelForm):
    
    class Meta:
        model=User
        fields=['username', 'email', 'password']
        """widgets = {
        'password': forms.PasswordInput()
        }"""

class DonorForm(forms.ModelForm):
    class Meta:
        model=models.Donor
        fields=['donor_first_name','donor_last_name','donor_postal','donor_bio_sex','donor_blood_type','donor_birthday','donor_weight','donor_height','donor_contact_phone','emergency_contact_name','emergency_contact_phone']

