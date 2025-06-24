from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path('<int:dia>', views.desafio_semana_numero),
    path('<str:dia>', views.desafio_semana, name="desafio_semanal"),

]