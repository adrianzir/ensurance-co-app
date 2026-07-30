from django.core.management.base import BaseCommand
from seguros.models import Seguro

class Command(BaseCommand):
    help = 'Poblar la base de datos con seguros de prueba iniciales'

    def handle(self, *args, **options):
        self.stdout.write('Iniciando carga de seguros de prueba...')
        
        # Eliminar seguros existentes para evitar duplicados en pruebas
        Seguro.objects.all().delete()
        
        seguros_datos = [
            {
                'titulo': 'Seguro de Auto Premium',
                'categoria': 'AUTO',
                'precio_mensual': 45.00,
                'cobertura_maxima': 50000.00,
                'icon_class': 'car',
                'descripcion_corta': 'Cobertura total contra todo riesgo para tu vehículo con asistencia 24/7.',
                'descripcion_detallada': (
                    'Nuestro Seguro de Auto Premium te ofrece la máxima protección en el camino.\n\n'
                    'Cubre daños a terceros, colisiones de cualquier tipo, robos totales o parciales, '
                    'y daños por desastres naturales o vandalismo. Incluye grúa de rescate ilimitada, '
                    'asistencia en ruta (cambio de neumáticos, paso de corriente, cerrajería vial) '
                    'y un vehículo de reemplazo por hasta 15 días mientras tu auto esté en taller.\n\n'
                    'Conduce con absoluta tranquilidad sabiendo que cuentas con el respaldo más completo del mercado.'
                ),
                'destacado': True
            },
            {
                'titulo': 'Seguro de Hogar Confort',
                'categoria': 'HOGAR',
                'precio_mensual': 35.00,
                'cobertura_maxima': 120000.00,
                'icon_class': 'home',
                'descripcion_corta': 'Protege la estructura de tu casa y todas tus pertenencias ante imprevistos.',
                'descripcion_detallada': (
                    'Tu hogar es tu santuario. Protégelo de manera integral con el Seguro Hogar Confort.\n\n'
                    'Este seguro brinda cobertura completa para la edificación (continente) y todos los bienes '
                    'que tienes dentro (contenido: electrodomésticos, muebles, ropa, tecnología) en casos de '
                    'incendio, sismos, inundaciones, explosiones y robo con fuerza. Además, incluye un paquete '
                    'de asistencia domiciliaria de urgencia (gasfitería, cerrajería, vidriería y electricidad) '
                    'con profesionales certificados disponibles las 24 horas.'
                ),
                'destacado': True
            },
            {
                'titulo': 'Seguro de Vida Pleno',
                'categoria': 'VIDA',
                'precio_mensual': 25.00,
                'cobertura_maxima': 80000.00,
                'icon_class': 'heart',
                'descripcion_corta': 'Garantiza el respaldo y bienestar financiero de tu familia en el futuro.',
                'descripcion_detallada': (
                    'El Seguro de Vida Pleno está pensado para darte la tranquilidad de saber que, pase lo que pase, '
                    'tu familia estará protegida económicamente.\n\n'
                    'Garantiza una indemnización libre de impuestos para tus beneficiarios en caso de fallecimiento, '
                    'así como coberturas adicionales para ti en caso de invalidez total y permanente por enfermedad '
                    'o accidente. También provee anticipos de capital para enfermedades graves y asesoría legal integral '
                    'para trámites sucesorios. Asegura el mañana de quienes más amas desde hoy.'
                ),
                'destacado': False
            },
            {
                'titulo': 'Seguro de Salud Vital',
                'categoria': 'SALUD',
                'precio_mensual': 55.00,
                'cobertura_maxima': 250000.00,
                'icon_class': 'activity',
                'descripcion_corta': 'Cobertura médica de primer nivel con acceso directo a clínicas privadas.',
                'descripcion_detallada': (
                    'La salud de tu familia es lo primero. Con el Seguro de Salud Vital cuentas con una cobertura médica superior.\n\n'
                    'Disfruta de copagos mínimos en consultas médicas generales y de especialidad, cobertura de hasta el 90% '
                    'en hospitalizaciones y cirugías programadas o de urgencia, y descuentos preferenciales de hasta el 70% '
                    'en medicamentos recetados. Además, obtienes telemedicina ilimitada gratuita para consultas rápidas desde '
                    'la comodidad de tu hogar, sin necesidad de salir ni hacer filas.'
                ),
                'destacado': True
            },
            {
                'titulo': 'Seguro de Tecnología Activa',
                'categoria': 'TECNOLOGIA',
                'precio_mensual': 12.00,
                'cobertura_maxima': 1800.00,
                'icon_class': 'smartphone',
                'descripcion_corta': 'Resguarda tu smartphone, notebook o tablet contra robos y daño accidental.',
                'descripcion_detallada': (
                    'Tus herramientas tecnológicas del día a día merecen estar seguras. Protégelas con Tecnología Activa.\n\n'
                    'Asegura tus dispositivos móviles (celulares, tablets, laptops, consolas portátiles) contra robos con violencia, '
                    'daños por caída accidental de líquidos, y roturas de pantalla. Ofrecemos reparación rápida en servicios técnicos '
                    'autorizados utilizando piezas 100% originales o la sustitución directa por un equipo de similares características '
                    'en caso de pérdida total o robo.'
                ),
                'destacado': False
            }
        ]
        
        for dato in seguros_datos:
            Seguro.objects.create(**dato)
            self.stdout.write(f"Seguro creado: '{dato['titulo']}'")
            
        self.stdout.write(self.style.SUCCESS('¡Base de datos poblada exitosamente!'))
