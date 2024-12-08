from django.shortcuts import render
from rest_framework import viewsets
from app.models import Tatuador, Cliente, Cita
from .serializers import TatuadorSerializer, ClienteSerializer, CitaSerializer
from rest_framework.permissions import AllowAny

class TatuadorViewSet(viewsets.ModelViewSet):
    queryset = Tatuador.objects.all()
    serializer_class = TatuadorSerializer
    permission_classes = [AllowAny]

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer