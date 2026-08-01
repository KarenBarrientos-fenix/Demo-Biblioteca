from django.db import models


class Grupo(models.Model):
    nombre = models.CharField(max_length=50)
    salon = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    grupo = models.ForeignKey(
        Grupo,
        on_delete=models.CASCADE,
        related_name='estudiantes'
    )
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    existencia = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, default='Sin ISBN')
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo


class Usuario(models.Model):
    TIPOS_USUARIO = [
        ('Estudiante', 'Estudiante'),
        ('Docente', 'Docente'),
    ]

    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    tipo = models.CharField(
        max_length=20,
        choices=TIPOS_USUARIO
    )

    def __str__(self):
        return self.nombre