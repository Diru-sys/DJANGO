from django.urls import path
from . import views

urlpatterns = [
    path("", views.principal, name="principal"),
    path("ji", views.ji, name="ji"),
    path("<int:pk>", views.detalles, name="detalles")
]
