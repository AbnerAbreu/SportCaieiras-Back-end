from rest_framework import viewsets
from eventos.models import Eventos
from Eventos.serializers import EventosSerializer


class EventosViewSet(viewsets.ModelViewSet):
    queryset = Eventos.objects.all()
    serializer_class = EventosSerializer