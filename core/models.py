from django.db import models

# Create your models here.
class Dueno(models.Model):
    nombre_dueno = models.CharField(max_length=80, verbose_name="Nombre del Dueño")
    rut_dueno = models.CharField(max_length=80, verbose_name="Rut del Dueño", unique=True)
    direccion_dueno = models.CharField(max_length=80, verbose_name="Direccion del Dueño")
    telefono_fijo = models.PositiveIntegerField(default=0, verbose_name="Telefono Fijo")
    celular = models.PositiveIntegerField(default=0, verbose_name="Celular")
    telefono_alternativo = models.PositiveIntegerField(default=0, verbose_name="Telefono Alternativo")
    
    def __str__(self):
        return self.nombre_dueno
    
    class Meta:
        verbose_name = "Dueño"
        verbose_name_plural = "Dueños"
        db_table = "dueno"
        ordering = ['id']

class Cliente(models.Model):
    dueno = models.ManyToManyField(Dueno)
    foto = models.ImageField(upload_to='archivos/imagenes', null=True, blank=True)
    carnet = models.FileField(upload_to='archivos/carnet', null=True, blank=True)
    nombres = models.CharField(max_length=80, verbose_name="Nombres")
    raza = models.CharField(max_length=50, verbose_name="Raza")
    edad = models.PositiveIntegerField(default=0, verbose_name="Edad")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    esterilizada_castrado = models.BooleanField(verbose_name="Esterilizada/Castrado", default=False)
    
    def __str__(self):
        return self.nombres
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        db_table = "cliente"
        ordering = ['id']

class Peluqueria(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    hipersensibilidad = models.BooleanField(verbose_name="Hipersensibilidad", default=False, null=True, blank=True)
    otitis = models.BooleanField(verbose_name="Otitis", default=False, null=True, blank=True)
    ulceras_ojos = models.BooleanField(verbose_name="Ulcera Ojos", default=False, null=True, blank=True)
    alergias = models.CharField(max_length=80, verbose_name="Alergias", null=True, blank=True)
    premios = models.CharField(max_length=80, verbose_name="Premios")
    fecha_registro = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombres
    
    class Meta:
        verbose_name = "Peluquería"
        verbose_name_plural = "Peluquerías"
        db_table = "peluqueria"
        ordering = ['id']

class Huesped(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    nombre_veterinario = models.CharField(max_length=80, verbose_name="Nombre del Veterinario")
    telefono_veterinario = models.PositiveIntegerField(default=0, verbose_name="Telefono del Veterinario")
    direccion_veterinario = models.CharField(max_length=80, verbose_name="Direccion del Veterinario")
    fecha_ultimo_celo = models.DateField(verbose_name="Fecha de ultimo celo")
    enfermedades = models.CharField(max_length=80, verbose_name="Enfermedades")
    medicamentos = models.CharField(max_length=80, verbose_name="Medicamentos")
    tolerancia_al_ejercicio = models.CharField(max_length=80, verbose_name="Tolerancia al Ejercicio")
    alimento = models.CharField(max_length=80, verbose_name="Alimento")
    frecuencia_alimentacion = models.CharField(max_length=80, verbose_name="Frecuencia de Alimentación")
    descripcion_del_caracter = models.CharField(max_length=80, verbose_name="Descripción del Caracter")
    fobias_miedos = models.CharField(max_length=80, verbose_name="Fobias o Miedos", null=True, blank=True)
    alergias_alimentos = models.CharField(max_length=80, verbose_name="Alergias a alimentos?", null=True, blank=True)
    alergias_medicamentos = models.CharField(max_length=80, verbose_name="Alergias a medicamentos?", null=True, blank=True)
    alergias_insectos = models.CharField(max_length=80, verbose_name="Alergias a insectos?", null=True, blank=True)
    vacuna_octuple = models.DateField(verbose_name="Vacuna Octuple", null=True, blank=True)
    vacuna_ar = models.DateField(verbose_name="Vacuna AR", null=True, blank=True)
    vacuna_kc = models.DateField(verbose_name="Vacuna KC", null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now=True)
    fecha_actualizacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Huesped"
        verbose_name_plural = "Huespedes"
        db_table = "huesped"
        ordering = ['id']
