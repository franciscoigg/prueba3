from django.contrib import admin
from app.models import Cliente,Tatuador,Cita

@admin.register(Tatuador)
class TatuadorAdmin(admin.ModelAdmin):
    list_display=('nombre','experiencia', 'estilo', 'email', 'telefono')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'telefono', 'direccion', 'email', 'presupuesto')

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('id_cita', 'id_tatuador', 'id_cliente', 'fecha_cita', 'estado', 'hora')
    


