from django.contrib import admin
from .models import Grupo, Estudiante, Producto, Libro, Usuario

admin.site.register(Grupo)
admin.site.register(Estudiante)
admin.site.register(Producto)
admin.site.register(Libro)
admin.site.register(Usuario)