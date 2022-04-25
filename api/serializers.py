from .models import Transacao
from rest_framework import serializers


class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = '__all__'

