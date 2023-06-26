from django.shortcuts import render
from .models import capteur, capteur_data
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
    capteurs = capteur.objects.get(pk=id)
    form = CapteurForm(model_to_dict(capteurs))
    if request.method == "POST":
        form = CapteurForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/capteur/info")
    else:
        return render(request, "capteur/update.html", {"form": form, "id": id})


def traitementupdate(request, id):
    capteurs = CapteurForm(request.POST)
    bak = capteur.objects.get(id=id)
    if capteur.is_valid():
        capteurs = capteur.save(commit=False)
        capteurs.id = id
        capteurs.macaddr = bak.macaddr
        capteurs.piece = bak.piece
        capteurs.save()
        return HttpResponseRedirect("/capteur/info.html")
    else:
        return render(request, "capteur/info.html", {"form": form, "id": id})

def filtre(request, id):
    data = capteur_data.objects.filter(sensor=id)
    return render(request, 'donnee/info.html', {'data': data})
