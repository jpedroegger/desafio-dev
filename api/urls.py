from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('detalhe/', views.detalhe_loja, name='detalhe'),

    path('lista_transacoes/', views.lista_transacoes, name='lista_transacoes'),
    path('detalhe_transacao/<int:pk>', views.detalhe_transacao, name='detalhe_transacao'),
]
