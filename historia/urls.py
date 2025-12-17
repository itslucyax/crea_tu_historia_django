"""
URL configuration for crea_historia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views # Importa las vistas (añadido pro itslucyax)
#Paso 7: Configurar las URLs de la aplicacion
urlpatterns = [
        path('', views.inicio, name='inicio'),
        path('bosque/', views.bosque, name='bosque'),
        path('cueva/', views.cueva, name='cueva'),
        path('final-bueno/', views.final_bueno, name='final_bueno'),
        path('final-malo/', views.final_malo, name='final_malo'),
]
