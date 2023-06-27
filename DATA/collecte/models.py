from django.db import models

class capteur(models.Model):
    address = models.CharField(unique=True, max_length=12)
    piece = models.CharField(max_length=50, null=False)
    emplacement = models.CharField(max_length=50)
    nom = models.CharField(max_length=50, blank=True, null=True)

    def dico(self):
        return {"emplacement": self.emplacement, "nom": self.nom}

    class Meta:
        managed = False
        db_table = 'capteur'



class capteur_data(models.Model):
    capteur = models.ForeignKey(capteur, models.DO_NOTHING, null=False)
    datetime = models.DateTimeField(null=False)
    temp = models.DecimalField(max_digits=5, decimal_places=2, null=False)

    class Meta:
        managed = False
        db_table = 'capteur_data'
