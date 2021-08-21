from django.shortcuts import render
from .models import Region
# Create your views here.

def home(request):
    return render(request,'home.html')

def regiones(request):
    #Llamar traer todas las regiones 
    regiones=Region.objects.all()
    return render(request, 'regiones.html',{'regiones':regiones}) 


def region_specific(request,region_nombre):
    region=Region.objects.filter(nombre__exact=region_nombre)
    
    return render(request,'reg_specific.html',{'region':region})

    
def term_cliente(request):
    #Llamar traer todas las regiones 
    regiones=Region.objects.all()

    """
    Paso de parametros por URL
    

    
    """
    return render(request,'term_cliente.html', {'regiones':regiones} )