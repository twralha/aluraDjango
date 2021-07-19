from django.shortcuts import render #padrão
from django.http import HttpResponse

def index(request):
    receitas = {
        1: 'Sucão de Frutas',
        2: 'Arroz com Feijão',
        3: 'Strogonoff de Frango',
        4: 'Bolo de Chocolate'
    }

    dados = {
        'nomes_receitas': receitas
    }
    return render(request, 'index.html', context=dados)

def receita(request):
    return render(request, 'receita.html')