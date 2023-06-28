import csv
from django.shortcuts import render
from .models import capteur, capteur_data
from . import models
from .forms import CapteurForm
from django.http import HttpResponseRedirect, HttpResponse
from matplotlib import pyplot as plt
from datetime import datetime
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
    sensors = capteur.objects.get(pk=id)
    form = CapteurForm(model_to_dict(sensors))
    if request.method == "POST":
        form = CapteurForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/collecte/donnee/")
    else:
        return render(request, "capteur/update.html", {"form": form, "id": id})

def traitementupdate(request, id):
    bak = capteur.objects.get(id=id)
    form = CapteurForm(request.POST, instance=bak)

    if form.is_valid():
        form.cleaned_data['address'] = bak.address
        form.cleaned_data['piece'] = bak.piece
        form.save()
        return HttpResponseRedirect("/capteur/info.html")
    else:
        return render(request, "capteur/info.html", {"form": form, "id": id})

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

def date(request):
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    data = models.capteur_data.objects.all()

    if start_date and end_date:
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        data = data.filter(datetime__range=(start_date, end_date))

    context = {'data': data}
    return render(request, 'donnees/info.html', context)


def graphique(request):
    data = capteur_data.objects.all()

    dates = [entry.datetime for entry in data]
    temperatures = [entry.temp for entry in data]

    plt.plot(dates, temperatures)

    plt.xlabel('Date et heure')
    plt.ylabel('Température (°C)')
    plt.title('Évolution de la température')

    plt.show()

    return HttpResponseRedirect("/collecte/donnee/")


