from django.urls import path
from . import views

urlpatterns = [
    path("", views.principal, name="principal"),
    path("<int:pk>/", views.detallesEntrada, name="detallesEntrada"),
    path("autores/", views.autores, name="autores"),
    path("autores/<int:pk>/", views.entradasAutor, name="entradasAutor"),
    path("categorias/<int:pk>/", views.detallesCategoria, name="detallesCategoria")
]
