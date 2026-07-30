from django.contrib import admin
from .models import Seguro, Contrato

@admin.register(Seguro)
class SeguroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'precio_mensual', 'cobertura_maxima', 'destacado')
    list_filter = ('categoria', 'destacado')
    search_fields = ('titulo', 'descripcion_corta', 'descripcion_detallada')

@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'seguro', 'fecha_contratacion', 'fecha_inicio', 'precio_pactado', 'estado')
    list_filter = ('estado', 'fecha_contratacion')
    search_fields = ('usuario__username', 'seguro__titulo')

