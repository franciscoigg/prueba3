from django.db import models
from django.core.validators import EmailValidator, MaxLengthValidator, MinValueValidator, RegexValidator
import re
from django.core.exceptions import ValidationError

def validate_telefono(value):
    if not re.match(r'^\d{9}$', value):
        raise ValidationError('El teléfono debe tener 9 dígitos.')

def validate_nombre(value):
    if not re.match(r'^[A-Za-zÁáÉéÍíÓóÚúÑñ\s]+$', value): 
        raise ValidationError('El nombre solo puede contener letras y espacios.')

class Tatuador(models.Model):
    id_tatuador=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=20, validators=[MaxLengthValidator(20), validate_nombre])
    experiencia=models.IntegerField(validators=[MinValueValidator(0)],help_text="Años.")
    estilo=models.CharField(max_length=20,validators=[MaxLengthValidator(20)])
    email=models.CharField(max_length=100,unique=True,validators=[EmailValidator()])
    telefono = models.CharField(max_length=9, validators=[validate_telefono])

    def __str__(self):
        return self.nombre

class Cliente(models.Model):
    id_cliente=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=20,validators=[MaxLengthValidator(20), validate_nombre])
    telefono = models.CharField(max_length=9, validators=[validate_telefono])
    direccion=models.CharField(max_length=20,validators=[MaxLengthValidator(20)])
    email=models.EmailField(max_length=100,unique=True, validators=[EmailValidator()])
    presupuesto=models.IntegerField(validators=[MinValueValidator(0)])

    def __str__(self):
        return self.nombre  

class Cita(models.Model):

    PENDIENTE = 'Pendiente'
    CONFIRMADA = 'Confirmada'
    CANCELADA = 'Cancelada'

    ESTADO_CHOICES = [
        (PENDIENTE, 'Pendiente'),
        (CONFIRMADA, 'Confirmada'),
        (CANCELADA, 'Cancelada'),
    ]

    id_cita = models.AutoField(primary_key=True)
    id_tatuador = models.ForeignKey(Tatuador, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_cita = models.DateField()
    estado = models.CharField(
        max_length=50,
        choices=ESTADO_CHOICES,
        default=PENDIENTE,
    )
    duracion = models.DurationField()
    descripcion = models.TextField(validators=[MaxLengthValidator(100),validate_nombre])
    hora = models.TimeField()

    def __str__(self):
        return f"Cita {self.id_cita} - {self.fecha_cita}"
