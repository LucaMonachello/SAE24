from . import models
from django.forms import ModelForm

class CapteurForm(ModelForm):
    class Meta:
        model = models.capteur
        fields = ('nom', 'emplacement')
        labels = {
            'nom' : ('Nom'),
            'emplacement': ('Emplacement'),

        }

