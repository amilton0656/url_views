from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

desafios_dia_semana = {
    'domingo': 'Desafio de domingo',
    'segunda': 'Desafio de segunda',
    'terca': 'Desafio de terca',
    'quarta': 'Desafio de  quarta',
    'quinta': 'Desafio de quinta',
    'sexta': None,
    'sabado': 'Desafio de sabado',
}

def desafio_semana_numero(request, dia):
    dias = list(desafios_dia_semana.keys())
    if dia > len(dias) or dia == 0:
        return HttpResponseNotFound("Dia inválido")
    dia_escolhido = dias[dia -1]
    redireciona_rota = reverse("desafio_semanal", args=[dia_escolhido])
    return HttpResponseRedirect(redireciona_rota)

def desafio_semana(request, dia):
    try:
        desafio = desafios_dia_semana[dia]
    except:
        # return HttpResponse("Para esse dia não há desafio")
        return render(request, '404.html')
    return render(request, "desafios/desafio.html", {
        'desafio': desafio,
        'dia': dia.capitalize()
    })

def index(request):
    dias = list(desafios_dia_semana.keys())
    return render(request, "desafios/index.html", {
        'dias':dias
    })
