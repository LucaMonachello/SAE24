from django.shortcuts import render
from .models import capteur, capteur_data
from . import models
from .forms import CapteurForm
from django.http import HttpResponseRedirect, HttpResponse
from django.forms.models import model_to_dict


def index(request):
    return render(request, 'index.html')


def capteurs(request):
    capteurs = capteur.objects.all()
    return render(request, 'capteur/info.html', {'capteurs': capteurs})


def donnee(request):
    data = capteur_data.objects.all()
    return render(request, 'donnees/info.html', {'data': data})


def update(request, id):
    capteur_obj = capteur.objects.get(pk=id)

    if request.method == "POST":
        form = CapteurForm(request.POST, instance=capteur_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/collecte/traitementupdate/")
    else:
        form = CapteurForm(instance=capteur_obj)

    return render(request, "capteur/update.html", {"form": form, "id": id})
def traitementupdate(request, id):
    lform = CapteurForm(request.POST)
    if lform.is_valid():
        Capteur = lform.save(commit=False)
        Capteur.id = id
        Capteur.save()
        return HttpResponseRedirect("/collecte/")
    else:
        return render(request, "capteur/update.html", {"form": lform, "id": id})

def filtre(request, id):
    data = capteur_data.objects.filter(capteur=id)
    return render(request, 'donnees/info.html', {'data': data})
