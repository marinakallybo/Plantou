from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("culturas/", views.listar_culturas, name="listar_culturas"),
    path("recomendar/", views.recomendar, name="recomendar"),
]