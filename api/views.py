from django.shortcuts import render
from rest_framework import generics
from .models import Persona
from .serializers import PersonaSerializer

from rest_framework.authentication import TokenAuthentication , SessionAuthentication
from rest_framework.permissions import IsAuthenticated 

class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

'''
1)
 - generics.ListCreateAPIView: vista basa en CLASE, lista y crea una instancia del modelo
 - queryset: las listas siempre van a requerir un query  para saber que datos van a listar.
 - serializer_class: el serializador es la clase que se encarga de transformar los modelos (queryset) en json o xml
 - serializer_class: el objeto de serializacion es la clase donde se definen los campos que va a mostrar o guardar en BD.
2) TokenAuthentication - IsAuthenticated
 
'''

