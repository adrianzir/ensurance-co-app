from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Seguro, Contrato
import datetime

class SeguroViewsTestCase(TestCase):
    def setUp(self):
        # Crear seguros de prueba
        self.seguro_auto = Seguro.objects.create(
            titulo="Seguro de Auto Test",
            categoria="AUTO",
            precio_mensual=30.00,
            cobertura_maxima=40000.00,
            descripcion_corta="Seguro de auto test",
            descripcion_detallada="Detalle del seguro de auto test",
            destacado=True
        )
        self.seguro_hogar = Seguro.objects.create(
            titulo="Seguro de Hogar Test",
            categoria="HOGAR",
            precio_mensual=20.00,
            cobertura_maxima=80000.00,
            descripcion_corta="Seguro de hogar test",
            descripcion_detallada="Detalle del seguro de hogar test",
            destacado=False
        )
        
        # Datos de usuario de prueba
        self.user_data = {
            'username': 'clientetest',
            'password': 'password123',
            'email': 'cliente@test.com',
            'first_name': 'Cliente',
            'last_name': 'Prueba'
        }
        self.user = User.objects.create_user(**self.user_data)

    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Seguro de Auto Test")
        self.assertContains(response, "Seguro de Hogar Test")

    def test_home_page_category_filter(self):
        response = self.client.get(reverse('home') + "?categoria=AUTO")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Seguro de Auto Test")
        self.assertNotContains(response, "Seguro de Hogar Test")

    def test_detail_page_loads(self):
        response = self.client.get(reverse('detalle', args=[self.seguro_auto.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.seguro_auto.titulo)
        self.assertContains(response, "Cobertura Máx.")
        self.assertContains(response, "$30,00")

    def test_anonymous_user_redirected_from_dashboard(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_anonymous_user_redirected_from_contract(self):
        response = self.client.get(reverse('contratar', args=[self.seguro_auto.id]))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_user_registration(self):
        # Cerrar sesión si la hay
        self.client.logout()
        
        registration_data = {
            'username': 'nuevousuario',
            'email': 'nuevo@usuario.com',
            'first_name': 'Nuevo',
            'last_name': 'Usuario',
            'password1': 'nuevoPass123!',
            'password2': 'nuevoPass123!'
        }
        
        response = self.client.post(reverse('registro'), registration_data)
        self.assertEqual(response.status_code, 302) # Redirección al dashboard
        self.assertTrue(User.objects.filter(username='nuevousuario').exists())

    def test_user_login(self):
        self.client.logout()
        
        login_data = {
            'username': 'clientetest',
            'password': 'password123'
        }
        
        response = self.client.post(reverse('login'), login_data)
        self.assertEqual(response.status_code, 302) # Redirección al dashboard
        
    def test_user_contract_insurance(self):
        # Iniciar sesión
        self.client.login(username='clientetest', password='password123')
        
        # Obtener página de contratación (GET)
        response = self.client.get(reverse('contratar', args=[self.seguro_auto.id]))
        self.assertEqual(response.status_code, 200)
        
        # Enviar formulario de contratación (POST)
        contract_data = {
            'fecha_inicio': datetime.date.today().strftime('%Y-%m-%d')
        }
        response = self.client.post(reverse('contratar', args=[self.seguro_auto.id]), contract_data)
        self.assertEqual(response.status_code, 302) # Redirección al dashboard
        
        # Verificar que el contrato se creó en la base de datos
        self.assertTrue(Contrato.objects.filter(usuario=self.user, seguro=self.seguro_auto).exists())
        
        # Verificar que aparece en el dashboard
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Seguro de Auto Test")
        self.assertContains(response, "Activo")

