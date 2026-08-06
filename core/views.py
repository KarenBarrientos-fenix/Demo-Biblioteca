from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Grupo, Estudiante, Libro
from .serializers import GrupoSerializer, EstudianteSerializer, LibroSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Grupo
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Libro

def index(request):
    return render(request, 'index.html')


@login_required
def lista_alumnos(request):
    todos_los_estudiantes = Estudiante.objects.all()
    estudiantes_activos = Estudiante.objects.filter(activo=True)

    contexto = {
        'todos': todos_los_estudiantes,
        'activos': estudiantes_activos
    }

    return render(request, 'alumnos.html', contexto)

@api_view(['GET', 'POST'])
def api_lista_grupos(request):

    if request.method == 'GET':
        grupos = Grupo.objects.all()
        serializer = GrupoSerializer(grupos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GrupoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_detalle_grupo(request, pk):
    try:
        grupo = Grupo.objects.get(pk=pk)
    except Grupo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GrupoSerializer(grupo)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = GrupoSerializer(
            grupo,
            data=request.data,
            partial=(request.method == 'PATCH')
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        grupo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@login_required
def lista_libros(request):
    libros = Libro.objects.all()

    return render(
        request,
        'libros.html',
        {'libros': libros}
    )

def iniciar_sesion(request):
    mensaje = ''

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:
            login(request, usuario)

            siguiente = request.POST.get('next')

            if siguiente:
                return redirect(siguiente)

            return redirect('lista_libros')

        mensaje = 'Usuario o contraseña incorrectos.'

    contexto = {
        'mensaje': mensaje,
        'next': request.GET.get('next', '')
    }

    return render(request, 'login.html', contexto)


def cerrar_sesion(request):
    logout(request)
    return redirect('login')

@api_view(['GET', 'POST'])
def api_lista_libros(request):

    if request.method == 'GET':
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LibroSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def api_detalle_libro(request, pk):

    try:
        libro = Libro.objects.get(pk=pk)

    except Libro.DoesNotExist:
        return Response(
            {'mensaje': 'Libro no encontrado'},
            status=status.HTTP_404_NOT_FOUND
        )

    if request.method == 'GET':
        serializer = LibroSerializer(libro)
        return Response(serializer.data)

    elif request.method in ['PUT', 'PATCH']:
        serializer = LibroSerializer(
            libro,
            data=request.data,
            partial=(request.method == 'PATCH')
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == 'DELETE':
        libro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
