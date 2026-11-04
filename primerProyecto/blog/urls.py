from django.urls import path
from . import views

urlpatterns = [
    path("", views.principal, name="principal"),
    path("<int:pk>/", views.detalles, name="detalles"),
    path("autores/", views.autores, name="autores"),
]
