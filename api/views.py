from django.shortcuts import render
from rest_framework import generics
from .models import Persona
from .serializers import PersonaSerializer

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token


from rest_framework.authentication import TokenAuthentication , SessionAuthentication
from rest_framework.permissions import IsAuthenticated 

class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [IsAuthenticated,]
    authentication_class = TokenAuthentication
    

class Login(FormView):
    template_name = 'login.html'
    form_class= AuthenticationForm
    success_url = reverse_lazy('api:persona')

    #redefino el metodo dispatch
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login, self).dispatch(request, *args, *kwargs)
        
    #redefino la vista basa en clases form_valid (FormView)
    def form_valid(self, form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        #bucamos token asocioado al usuario
        token,_ = Token.objects.get_or_create(user = user)

        if token:
            login(self.request, form.get_user())
            return super(Login,self).form_valid(form)

'''
1)
 - generics.ListCreateAPIView: vista basa en CLASE, lista y crea una instancia del modelo
 - queryset: las listas siempre van a requerir un query  para saber que datos van a listar.
 - serializer_class: el serializador es la clase que se encarga de transformar los modelos (queryset) en json o xml
 - serializer_class: el objeto de serializacion es la clase donde se definen los campos que va a mostrar o guardar en BD.
2) Login
 - form_valid: se aplicaran los filtros necesarios 
3) IsAuthenticated
 - TokenAuthentication - 
 
'''

