from django.shortcuts import render
from .models import Region
# Create your views here.

def home(request):
    return render(request,'home.html')

def regiones(request):
    #Llamar traer todas las regiones 
    regiones=Region.objects.all()
    return render(request, 'regiones.html',{'regiones':regiones}) 

def term_cliente(request):
    #Llamar traer todas las regiones 
    regiones=Region.objects.all()
    return render(request,'term_cliente.html', {'regiones':regiones} )