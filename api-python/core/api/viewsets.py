from django.db.models import Model
from rest_framework.viewsets import ModelViewSet
from core.models import PontoTuristico
from .serializers import PontoTuristicoSerializer

class PontoTuristicoViewSet(ModelViewSet):


    queryset = PontoTuristico.objects.all()
    serializer_class = PontoTuristicoSerializer
