from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('detalhe/', views.detalhe_loja, name='detalhe'),

    path('api/', views.lista_api, name='lista_transacoes'),
    path('api/<int:pk>', views.detalhe_api, name='detalhe_transacao'),]
