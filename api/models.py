from datetime import datetime
import os

from django.db import models


TIPOS_DE_TRANSACAO = [
    (1, 'Débito'), (2, 'Boleto'), (3, 'Financiamento'), (4, 'Crédito'), (5, 'Recebimento Empréstimo'),
    (6, 'Vendas'), (7, 'Recebimento TED'), (8, 'Recebimento DOC'), (9, 'Aluguel'),
]

NATUREZA = {'adicao': ['1', '4', '5', '6', '7', '8'], 'subtracao': ['2', '3', '9']}


def handle_uploaded_file(f):
    f.name = f.name.replace(' ', '_')
    caminho = '/'.join(('media', f.name))

    with open(caminho, 'r', encoding='utf-8') as file:

        for linha in file.readlines():
            linha = linha.rstrip('\n')

            if len(linha) > 80 or linha.isspace() or len(linha) < 50:
                continue

            arquivo = formatar_arquivo(linha)

            if arquivo['tipo'] in NATUREZA['subtracao']:
                arquivo['valor'] = float(arquivo['valor']) * -1

            arquivo_formatado = arquivo
            Transacao.objects.get_or_create(**arquivo_formatado)


def formatar_arquivo(linha):
    return {
        'tipo': linha[0], 'data': datetime.strptime(linha[1:9], '%Y%m%d'),
        'valor': float(linha[9:19]) / 100, 'cpf': linha[19:30], 'cartao': linha[30:42],
        'hora': datetime.strptime(linha[42:48], '%H%M%S'), 'dono': linha[48:62], 'loja': linha[62:80]
    }


def upload_path(instance, filename):
    nome, formato = os.path.splitext(filename)
    return f'{nome}{formato}'


class Transacao(models.Model):
    tipo = models.PositiveIntegerField(verbose_name='Tipo de Transação', choices=TIPOS_DE_TRANSACAO)
    data = models.DateField()
    valor = models.DecimalField(decimal_places=2, max_digits=10)
    cpf = models.CharField(max_length=11, verbose_name='CPF')
    cartao = models.CharField(max_length=12, verbose_name='Cartão')
    hora = models.TimeField()
    dono = models.CharField(max_length=14, verbose_name='Dono da Loja')
    loja = models.CharField(max_length=19, verbose_name='Nome da Loja')

    def __str__(self):
        return f'{self.loja}'

    class Meta:
        verbose_name = 'Transação'
        verbose_name_plural = "Transações"


class File(models.Model):
    arquivo = models.FileField(upload_to=upload_path)
