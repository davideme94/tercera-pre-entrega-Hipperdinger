from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Camiseta, Short, Botin
from .forms import CamisetaForm, BotinForm, ShortsForm
from django.urls import reverse


def indumentaria_lista(request):
    lista_camisetas = Camiseta.objects.all()  
    lista_shorts = Short.objects.all()        
    lista_botines = Botin.objects.all()       
 
    todas_las_indumentarias = list(lista_camisetas) + list(lista_shorts) + list(lista_botines)
    
    return render(request, 'indumentarias/indumentaria_lista.html', {"posts": todas_las_indumentarias})


def agregar_camiseta(request):
    if request.method == 'POST':
        form = CamisetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('camisetas:list')
    else:
        form = CamisetaForm()
    return render(request, 'indumentarias/agregar_camiseta.html', {'form': form})

def agregar_botin(request):
    if request.method == 'POST':
        form = BotinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('botines:list')
    else:
        form = BotinForm()
    return render(request, 'indumentarias/agregar_botin.html', {'form': form})

def agregar_shorts(request):
    if request.method == 'POST':
        form = ShortsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shorts:list')
    else:
        form = ShortsForm()
    return render(request, 'indumentarias/agregar_shorts.html', {'form': form})

def busquedatipo(request):
    return render(request, "indumentarias/busquedatipo.html")

def buscar(request):
    if request.GET.get("tipo"):
        tipo = request.GET["tipo"]

        camisetas = Camiseta.objects.filter(tipo__icontains=tipo)
        shorts = Short.objects.filter(tipo__icontains=tipo)
        botines = Botin.objects.filter(tipo__icontains=tipo)

        resultados = list(camisetas) + list(shorts) + list(botines)

        return render(request, "indumentarias/resultadobusqueda.html", {"resultados": resultados, "tipo": tipo})
    else:
        return HttpResponse("No enviaste datos")