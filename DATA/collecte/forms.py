from . import models
from django.forms import ModelForm
from django import forms

class CapteurForm(ModelForm):
    class Meta:
        model = models.capteur
        fields = ('emplacement', 'nom')
        labels = {
            'nom': 'Nom',
            'emplacement': 'Emplacement'
        }