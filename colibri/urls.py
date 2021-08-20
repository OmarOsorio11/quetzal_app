from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('term_cliente/', views.term_cliente, name='term_cliente'),
    path('regiones/', views.regiones, name='regiones'),
    
]