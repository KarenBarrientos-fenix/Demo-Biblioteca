from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciar_sesion, name='inicio'),

    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('libros/', views.lista_libros, name='lista_libros'),

    # API de libros
    path(
        'api/libros/',
        views.api_lista_libros,
        name='api_lista_libros'
    ),

    path(
        'api/libros/<int:pk>/',
        views.api_detalle_libro,
        name='api_detalle_libro'
    ),

    # API de grupos que ya tenías
    path(
        'api/grupo/',
        views.api_lista_grupos,
        name='api_lista_grupos'
    ),

    path(
        'api/grupo/<int:pk>/',
        views.api_detalle_grupo,
        name='api_detalle_grupo'
    ),
]