from django.shortcuts import render
from .models import Cultura
from .services import recomendar_culturas


def listar_culturas(request):
    culturas = Cultura.objects.all().order_by("nome")

    return render(request, "recomendador/listar_culturas.html", {
        "culturas": culturas
    })


def recomendar(request):
    recomendacoes = None

    if request.method == "POST":
        temperatura = float(request.POST.get("temperatura"))
        solo = request.POST.get("solo")
        umidade = request.POST.get("umidade")

        culturas = Cultura.objects.all()
        recomendacoes = recomendar_culturas(culturas, temperatura, solo, umidade)[:5]

    return render(request, "recomendador/recomendar.html", {
        "recomendacoes": recomendacoes
    })

def home(request):
    return render(request, "recomendador/home.html")