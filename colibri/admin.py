from django.contrib import admin
from .models import Clima,Region,Productor,Producto,Presentacion
# Register your models here.
admin.site.register(Clima)
admin.site.register(Region)
admin.site.register(Productor)
admin.site.register(Producto)
admin.site.register(Presentacion)