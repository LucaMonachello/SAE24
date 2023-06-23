from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import table1Form
from . import models

def ajout(request):
        form = table1Form()
        return render(request, "CRUD1/ajout.html", {"form": form})

def traitement(request):
    lform = table1Form(request.POST)
    if lform.is_valid():
        table1 = lform.save()
        return HttpResponseRedirect("/collecte/")
    else :
        return render(request, "collecte/CRUD1/ajout.html", {"form": lform})

def index(request):
    liste = list(models.table1.objects.all())
    return render(request, "CRUD1/index.html", {"liste": liste})

def affiche(request, id):
    table1 = models.table1.objects.get(pk=id)
    return render(request, "CRUD1/affiche.html", {"table1": table1})

def update(request, id):
    table1 = models.table1.objects.get(pk=id)
    form = table1Form(table1.dico())
    return render(request,"CRUD1/update.html",{"form": form, "id": id})

def traitementupdate(request, id):
    lform = table1Form(request.POST)
    if lform.is_valid():
        table1 = lform.save(commit=False)
        table1.id = id
        table1.save()
        return HttpResponseRedirect("/collecte/")
    else:
        return render(request, "CRUD1/update.html", {"form": lform, "id": id})

def delete(request, id):
    table1 = models.table1.objects.get(pk=id)
    table1.delete()
    return HttpResponseRedirect("/collecte/")
