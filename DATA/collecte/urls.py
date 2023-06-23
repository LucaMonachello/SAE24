from . import views, views_crud
from django.urls import path

urlpatterns = [
    path("ajout/", views.ajout),
    path("traitement/", views.traitement),
    path("", views.index),
    path("affiche/<int:id>/", views.affiche),
    path("update/<int:id>/", views.update),
    path("traitementupdate/<int:id>/", views.traitementupdate),
    path("delete/<int:id>/", views.delete),
    #####
    path("ajoutcrud/", views_crud.ajoutcrud),
    path("traitementcrud/", views_crud.traitementcrud),
    path("indexcrud/", views_crud.indexcrud),
    path("affichecrud/<int:id>/", views_crud.affichecrud),
    path("updatecrud/<int:id>/", views_crud.updatecrud),
    path("traitementupdatecrud/<int:id>/", views_crud.traitementupdatecrud),
    path("deletecrud/<int:id>/", views_crud.deletecrud),
    ]