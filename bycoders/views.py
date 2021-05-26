from django.shortcuts import render
from ficheros_py.cargar import *
from bycoders.models import *
import pymsgbox


# Create your views here.

def aplicacao(request):
    ops = Operacao.objects.all()
    return render(request, 'index.html', {'dados': ops})

def cargar(request):

    dados = CARGAR.carregar()
    for op in dados:
        ope = Operacao(loja=op.loja, dono=op.dono, tipo=op.tipo, cartao=op.cartao, cpf=op.cpf, valor=op.valor, data=op.data, hora=op.hora, total=op.total)
        ope.save()
    pymsgbox.alert('Dados Adicionados!', 'Confirmação')
    ops = Operacao.objects.all()
    return render(request, 'index.html', {'dados': ops})













