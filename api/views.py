from django.shortcuts import render, redirect
from .models import Transacao, handle_uploaded_file
from django.db.models import Sum
from .forms import FileForm

from .serializers import TransacaoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


def index(request):
    if request.method != 'POST':
        form = FileForm()
        transacoes = Transacao.objects.order_by('-data')
        return render(request, 'api/index.html', {'form': form, 'transacoes': transacoes})

    form = FileForm(request.POST, request.FILES)

    if not form.is_valid():
        form = FileForm(request.POST)
        return render(request, 'api/index.html', {'form': form})

    form.save()
    handle_uploaded_file(request.FILES['arquivo'])
    return redirect('index')


def detalhe_loja(request):

    detalhes = Transacao.objects.values('loja').annotate(soma=Sum('valor'))

    return render(request, 'api/detalhe.html', {'detalhes': detalhes})


@api_view(['GET'])
def lista_transacoes(request):
    if request.method == 'GET':
        transacoes = Transacao.objects.all()
        serializers = TransacaoSerializer(transacoes, many=True)
        return Response(serializers.data)


@api_view(['GET'])
def detalhe_transacao(request, pk):

    try:
        transacao = Transacao.objects.get(pk=pk)
    except Transacao.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializers = TransacaoSerializer(transacao)
        return Response(serializers.data)
