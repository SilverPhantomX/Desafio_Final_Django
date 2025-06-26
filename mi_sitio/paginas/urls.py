from django.urls import path
from . import views



urlpatterns = [
    path ("",views.inicio, name = "inicio"),
    path ("Paquita/",views.Paqui, name = "Paquita"),
    path ("Inky/",views.Inky, name = "Inky"),
    path ("Cirila/",views.Cirila, name = "Cirila"),
]