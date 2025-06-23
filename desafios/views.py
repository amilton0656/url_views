from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

desafios_dia_semana = {
    'domingo': 'Desafio de domingo',
    'segunda': 'Desafio de segunda',
    'terca': 'Desafio de terca',
    'quarta': 'Desafio de  quarta',
    'quinta': 'Desafio de quinta',
    'sexta': 'Desafio de sexta',
    'sabado': 'Desafio de sabado',
}

def desafio_semana_numero(request, dia):
    dias = list(desafios_dia_semana.keys())
    if dia > len(dias) or dia == 0:
        return HttpResponseNotFound("Dia inválido")
    dia_escolhido = dias[dia -1]
    return HttpResponseRedirect("/desafios/" + dia_escolhido)

def desafio_semana(request, dia):
    try:
        desafio = desafios_dia_semana[dia]
    except:
        return HttpResponse("Para esse dia não há desafio")
    return HttpResponseNotFound(desafio)
