from django.db import models
from django.contrib.auth.models import User

class Seguro(models.Model):
    CATEGORIAS = [
        ('AUTO', 'Seguro de Auto'),
        ('HOGAR', 'Seguro de Hogar'),
        ('VIDA', 'Seguro de Vida'),
        ('SALUD', 'Seguro de Salud'),
        ('TECNOLOGIA', 'Seguro de Tecnología'),
    ]

    titulo = models.CharField(max_length=100, verbose_name="Título")
    descripcion_corta = models.CharField(max_length=255, verbose_name="Descripción Corta")
    descripcion_detallada = models.TextField(verbose_name="Descripción Detallada")
    precio_mensual = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Mensual")
    cobertura_maxima = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Cobertura Máxima")
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='AUTO', verbose_name="Categoría")
    imagen_url = models.URLField(max_length=500, blank=True, null=True, verbose_name="URL de Imagen")
    icon_class = models.CharField(max_length=50, default='shield', verbose_name="Icono (Lucide/FontAwesome)")
    destacado = models.BooleanField(default=False, verbose_name="Destacado")

    class Meta:
        verbose_name = "Seguro"
        verbose_name_plural = "Seguros"

    def __str__(self):
        return f"{self.titulo} ({self.get_categoria_display()})"


class Contrato(models.Model):
    ESTADOS = [
        ('ACTIVO', 'Activo'),
        ('PENDIENTE', 'Pendiente de Pago'),
        ('CANCELADO', 'Cancelado'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contratos', verbose_name="Cliente")
    seguro = models.ForeignKey(Seguro, on_delete=models.CASCADE, related_name='contratos', verbose_name="Seguro")
    fecha_contratacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Contratación")
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio de Cobertura")
    precio_pactado = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio Pactado")
    estado = models.CharField(max_length=20, choices=ESTADOS, default='ACTIVO', verbose_name="Estado")

    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"

    def __str__(self):
        return f"Contrato #{self.id} - {self.usuario.username} ({self.seguro.titulo})"

