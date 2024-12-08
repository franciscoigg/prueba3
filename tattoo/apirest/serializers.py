from rest_framework import serializers
from app.models import Tatuador, Cliente, Cita

class TatuadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tatuador
        fields = ['id_tatuador', 'nombre', 'experiencia', 'estilo', 'email', 'telefono']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id_cliente', 'nombre', 'telefono', 'direccion', 'email', 'presupuesto']

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = ['id_cita', 'id_tatuador', 'id_cliente', 'fecha_cita', 'estado', 'duracion', 'descripcion', 'hora']