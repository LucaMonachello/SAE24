from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("capteur/",views.capteurs),
    path('update/<int:id>/', views.update),
    path('traitementupdate/<int:id>/', views.traitementupdate),
    path("donnee/", views.donnee),
    path('filtre/<int:id>/', views.filtre),
]