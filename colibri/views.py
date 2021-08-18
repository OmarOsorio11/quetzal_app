from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def term_cliente(request):

    return render(request,'term_cliente.html' )