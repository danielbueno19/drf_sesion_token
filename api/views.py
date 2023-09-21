from django.shortcuts import render
from rest_framework import generics
from .models import Persona
from .serializers import PersonaSerializer

class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

'''
1)
 - generics.ListCreateAPIView: vista basa en CLASE, lista y crea una instancia del modelo
 - queryset: las listas siempre van a requerir un query  para saber que datos van a listar.
 - serializer_class: el serializador es la clase que se encarga de transformar los modelos (queryset) en json o xml
'''