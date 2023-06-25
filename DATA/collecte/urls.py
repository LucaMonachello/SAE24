from . import views
from django.urls import path

urlpatterns = [
    path("capteur/", views.capteur),
    path("donnee/", views.donnee),
    path("", views.index),
    path("filtre/<int:id>/", views.filtre),
    path("update/<int:id>/", views.update),
    path("traitementupdate/<int:id>/", views.traitementupdate),
    ]