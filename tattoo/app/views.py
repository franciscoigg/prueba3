from django.shortcuts import render,redirect
from app.models import Tatuador,Cita,Cliente
from app.forms import TatuadorForm,CitaForm,ClienteForm

# Create your views here.

def index(request):
    return render(request,'app/index.html')

def lista_tatuadores(request):
    tatuadores=Tatuador.objects.all()
    return render(request,'app/tatuadores.html',{'tatuadores':tatuadores})

def lista_clientes(request):
    clientes=Cliente.objects.all()
    return render(request,'app/clientes.html',{'clientes':clientes})

def lista_citas(request):
    citas=Cita.objects.all()
    return render(request,'app/citas.html',{'citas':citas})

def agregar_tatuador(request):
    if request.method=='POST':
        form=TatuadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tatuadores')
    else:
        form=TatuadorForm()
    return render(request,'crud/agregar_tatuador.html',{'form':form})

def eliminar_tatuador(request,id):
    tatuador = Tatuador.objects.get(id_tatuador=id)  
    tatuador.delete()
    return redirect('tatuadores')

def actualizar_tatuador(request,id):
    tatuador=Tatuador.objects.get(id_tatuador=id)
    form=TatuadorForm(instance=tatuador)
    if request.method=='POST':
        form=TatuadorForm(request.POST,instance=tatuador)
        if form.is_valid():
            form.save()
        return redirect('tatuadores')
    data={'form':form}
    return render(request,'crud/agregar_tatuador.html',{'form':form})

def agregar_cliente(request):
    if request.method=='POST':
        form=ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form=ClienteForm()
    return render(request,'crud/agregar_cliente.html',{'form':form})

def eliminar_cliente(request,id):
    cliente=Cliente.objects.get(id_cliente=id)
    cliente.delete()
    return redirect('clientes')

def actualizar_cliente(request,id):
    cliente=Cliente.objects.get(id_cliente=id)
    form=ClienteForm(instance=cliente)
    if request.method=='POST':
        form=ClienteForm(request.POST,instance=cliente)
        if form.is_valid():
            form.save()
        return redirect('clientes')
    data={'form':form}
    return render(request,'crud/agregar_cliente.html',{'form':form})

def agregar_cita(request):
    if request.method=='POST':
        form=CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('citas')
    else:
        form=CitaForm()
    return render(request,'crud/agregar_cita.html',{'form':form})

def eliminar_cita(request,id):
    cita=Cita.objects.get(id_cita=id)
    cita.delete()
    return redirect('citas')

def actualizar_cita(request,id):
    cita=Cita.objects.get(id_cita=id)
    form=CitaForm(instance=cita)
    if request.method=='POST':
        form=CitaForm(request.POST,instance=cita)
        if form.is_valid():
            form.save()
        return redirect('citas')
    data={'form':form}
    return render(request,'crud/agregar_cita.html',data)
