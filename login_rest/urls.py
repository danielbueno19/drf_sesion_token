from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views
from api.views import Login, Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('api.urls', 'api'))),
    path('api_generete_token/', views.obtain_auth_token),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
]


'''
1) rest_framework.authtoken: genera token de manera automatica el cual debe enviarse via POST de otra forma fallara
2) ruta de login
'''