from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import table2Form
from . import models

def ajoutcrud(request):
        form = table2Form()
        return render(request, "CRUD2/ajout.html", {"form": form})

def traitementcrud(request):
    lform = table2Form(request.POST)
    if lform.is_valid():
        table2 = lform.save()
        return HttpResponseRedirect("/collecte/")
    else :
        return render(request, "collecte/CRUD2/ajout.html", {"form": lform})

def indexcrud(request):
    liste = list(models.table2.objects.all())
    return render(request, "CRUD2/index.html", {"liste": liste})

def affichecrud(request, id):
    table2 = models.table2.objects.get(pk=id)
    return render(request, "CRUD2/affiche.html", {"table2": table2})

def updatecrud(request, id):
    table2 = models.table2.objects.get(pk=id)
    form = table2Form(table2.dico())
    return render(request,"CRUD2/update.html",{"form": form, "id": id})

def traitementupdatecrud(request, id):
    lform = table2Form(request.POST)
    if lform.is_valid():
        table2 = lform.save(commit=False)
        table2.id = id
        table2.save()
        return HttpResponseRedirect("/collecte/")
    else:
        return render(request, "CRUD2/update.html", {"form": lform, "id": id})

def deletecrud(request, id):
    table2 = models.table2.objects.get(pk=id)
    table2.delete()
    return HttpResponseRedirect("/collecte/")
