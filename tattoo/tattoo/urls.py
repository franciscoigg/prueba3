"""tattoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='inicio'),
    path('tatuadores/',views.lista_tatuadores,name='tatuadores'),
    path('clientes/',views.lista_clientes,name='clientes'),
    path('citas/',views.lista_citas,name='citas'),
    path('agregar_tatuador/',views.agregar_tatuador,name='agregar_tatuador'),
    path('eliminar_tatuador/<int:id>/',views.eliminar_tatuador,name='eliminar_tatuador'),
    path('actualizar_tatuador/<str:id>/', views.actualizar_tatuador,name='actualizar_tatuador'),
    path('agregar_cliente/',views.agregar_cliente,name='agregar_cliente'),
    path('eliminar_cliente/<str:id>/',views.eliminar_cliente,name='eliminar_cliente'),
    path('actualizar_cliente/<str:id>/', views.actualizar_cliente,name='actualizar_cliente'),
    path('agregar_cita/',views.agregar_cita,name='agregar_cita'),
    path('eliminar_cita/<str:id>/',views.eliminar_cita,name='eliminar_cita'),
    path('actualizar_cita/<str:id>/', views.actualizar_cita,name='actualizar_cita'),

]
