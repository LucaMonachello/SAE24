from django.db import models

class table1(models.Model):
    piece = models.CharField(max_length=255, null=False)
    emplacement = models.CharField(max_length=255, null=False)


    def __str__(self):
        chaine = f"{self.piece} dans {self.emplacement}"
        return chaine

    def dico(self):
        return {"piece": self.piece, "emplacement": self.emplacement}


class table2(models.Model):
    date = models.DateField(null=False)
    temps = models.TimeField(null=False)
    temp = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    nom = models.ForeignKey(table1, on_delete=models.CASCADE)
    def __str__(self):
        chaine = f"{self.nom} {self.date} {self.temps} {self.temp} {self.temp}"
        return chaine

    def dico(self):
        return {"date": self.date, "temps": self.temps, "temps": self.temp, "nom": self.nom}
