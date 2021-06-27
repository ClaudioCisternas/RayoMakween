from django.shortcuts import render

from rest_framework import generics
from rayoMakween.models import Trabajo
from .serializers import TrabajoSerializers

# Create your views here.

class TrabajosViewSet(generics.ListCreateAPIView):
    queryset = Trabajo.objects.all()
    serializer_class = TrabajoSerializers

class TrabajosFiltroViewSet(generics.ListAPIView):
    serializer_class = TrabajoSerializers
    def get_querryset(self):
        nombre_trabajo = self.kwargs['nombre']
        return Trabajo.objects.filter(nombre=nombre_trabajo)