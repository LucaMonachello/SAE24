from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("capteur/",views.capteurs),
    path('capteur/update/<int:id>', views.update),
    path('capteur/info/<int:id>', views.traitementupdate),
    path("donnee/", views.donnee),
    path('donnees/info/<int:id>', views.filtre),
]