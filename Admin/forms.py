from django import forms

from . import models


class BloodForm(forms.ModelForm):
    class Meta:
        model = models.Stock
        fields = ['bloodgroup', 'unit']
