from django import forms
from app.models import Tatuador,Cliente,Cita

class TatuadorForm(forms.ModelForm):
    class Meta:
        model=Tatuador
        fields=['nombre','experiencia','estilo','email','telefono']

class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields=['nombre','telefono','direccion','email','presupuesto']

class CitaForm(forms.ModelForm):
    class Meta:
        model=Cita
        fields=['id_tatuador','id_cliente','fecha_cita','estado','duracion','descripcion','hora']
        widgets={
            'fecha_cita':forms.DateInput(attrs={'type':'date'}),
            'hora':forms.TimeInput(attrs={'type':'time'}),
            'duracion': forms.TextInput(attrs={'placeholder': 'hh:mm:ss'}),
        }