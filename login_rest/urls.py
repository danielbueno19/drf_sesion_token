from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api_generete_token/', views.obtain_auth_token),
]


'''
1) rest_framework.authtoken: genera token de manera automatica el cual debe enviarse via POST de otra forma fallara
'''