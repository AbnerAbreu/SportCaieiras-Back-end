from rest_framework import serializers
from colaborador.models import Colaborador


class ColaboradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colaborador
        fields = ['__All__']
