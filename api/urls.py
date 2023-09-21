from django.urls import path
from .views import PersonaList

urlpatterns = [
    path('persona/',PersonaList.as_view(),name='persona'),
]

'''
1) enlazo la ruta PersonaList al URL raiz del proyecto
'''