from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class table1Form(ModelForm):
    class Meta:
        model = models.table1
        fields = ('piece', 'emplacement')
        labels = {
            'piece' : _('Pièce'),
            'emplacement': _('Emplacement'),

        }

class table2Form(ModelForm):
    class Meta:
        model = models.table2
        fields = ('date', 'temps', 'temp', 'nom')
        labels = {
            'date' : _('Date'),
            'temps' : _('Temps') ,
            'temp' : _('Température'),
            'nom' : _('Nom du capteur')
        }
