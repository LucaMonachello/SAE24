from datetime import datetime
from pkgutil import get_data
import csv
from django.shortcuts import render
from .models import capteur, capteur_data
from . import models
from .forms import CapteurForm
from django.http import HttpResponseRedirect, HttpResponse
from django.db.models import Q



def index(request):
    return render(request, 'index.html')


def capteurs(request):
    capteurs = capteur.objects.all()
    return render(request, 'capteur/info.html', {'capteurs': capteurs})


def donnee(request):
    data = capteur_data.objects.all()
    return render(request, 'donnees/info.html', {'data': data})


def update(request, id):
    capteur = models.capteur.objects.get(pk=id)
    form = CapteurForm(capteur.dico())
    return render(request,"capteur/update.html",{"form": form, "id": id})

def traitementupdate(request, id):
    lform = CapteurForm(request.POST)
    if lform.is_valid():
        capteur = lform.save(commit=False)
        capteur.id = id
        capteur.save()
        return HttpResponseRedirect("/collecte/")
    else:
        return render(request, "capteur/update.html", {"form": lform, "id": id})

def filtre(request, id):
    data = capteur_data.objects.filter(capteur=id)
    return render(request, 'donnees/info.html', {'data': data})


def generate_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Capteur Address', 'Capteur Piece', 'Capteur Emplacement', 'Capteur Nom', 'Data Datetime', 'Data Temp'])

    data = capteur_data.objects.select_related('capteur').all()
    for item in data:
        writer.writerow([
            item.capteur.address,
            item.capteur.piece,
            item.capteur.emplacement,
            item.capteur.nom,
            item.datetime,
            item.temp
        ])

    return response