# Frontal Seguros - Portal de Gestión y Contratación de Pólizas

Este es un portal web de seguros moderno desarrollado con **Python** y **Django**. Permite a los visitantes explorar y buscar una amplia variedad de seguros (Auto, Hogar, Vida, Salud, Tecnología). Si deciden adquirir alguno, el sistema les exige registrarse o iniciar sesión, guiándolos a través de una experiencia de contratación con pasarela de pago simulada y un panel de cliente personal (dashboard).

---

##  Diseño y Experiencia de Usuario (UI/UX)

La plataforma cuenta con un diseño premium y adaptativo (responsive):
* **Fondos**: Mezclas limpias de blanco puro (`#ffffff`) y azul grisáceo suave (`#f8fafc`).
* **Branding y Acentuación**: Azul corporativo (`#1d4ed8`) y tonos morados/índigo (`#4f46e5`).
* **Estados**: Verde esmeralda (`#16a34a`) para pólizas activas e hitos de aprobación.
* **Tipografía**: Fuentes modernas `Outfit` (para títulos llamativos) e `Inter` (para textos limpios de alta legibilidad).
* **Interactividad**: Efectos hover tridimensionales en tarjetas, barra de navegación estilo *glassmorphism* (esmerilada) y un simulador de tarjeta de crédito visual en tiempo real durante la compra.

---

## Estructura del Proyecto

A continuación se detalla el propósito de cada carpeta y archivo dentro de la estructura de **Frontal Seguros**:

```
Frontal seguros/
├── .venv/                              # Entorno virtual aislado para dependencias de Python
├── db.sqlite3                          # Base de datos relacional ligera SQLite del proyecto
├── manage.py                           # Utilidad de línea de comandos de Django para administrar el proyecto
├── requirements.txt                    # Archivo con dependencias y librerías externas (Django, Pillow)
├── README.md                           # Documento explicativo del proyecto (este archivo)
│
├── seguros_project/                    # Directorio de configuración principal de Django
│   ├── __init__.py                     # Indica a Python que esta carpeta es un paquete
│   ├── asgi.py                         # Configuración para servidores web asíncronos (ASGI)
│   ├── settings.py                     # Ajustes principales del proyecto (base de datos, idioma, apps, estáticos)
│   ├── urls.py                         # Enrutador principal de URLs a nivel de proyecto
│   └── wsgi.py                         # Configuración para servidores web síncronos tradicionales (WSGI)
│
└── seguros/                            # Aplicación principal del portal de seguros
    ├── __init__.py                     # Indica que seguros es un paquete de Python
    ├── admin.py                        # Registro y personalización de los modelos en el panel de administración
    ├── apps.py                         # Configuración de los metadatos de la aplicación "seguros"
    ├── forms.py                        # Formulario de registro de cliente y formulario de contratación
    ├── models.py                       # Definición de tablas de BBDD: Seguro (pólizas) y Contrato (adquisiciones)
    ├── tests.py                        # Pruebas unitarias automatizadas (8 test de flujos, vistas y lógica)
    ├── urls.py                         # Enrutador local de URLs específicas de la aplicación
    ├── views.py                        # Lógica de las páginas (catálogo, detalle, auth, contratación, dashboard)
    │
    ├── management/                     # Comandos personalizados de administración de Django
    │   └── commands/
    │       └── seed_data.py            # Comando "seed_data" para cargar seguros iniciales de prueba en la BBDD
    │
    ├── static/                         # Archivos estáticos de frontend (CSS, JS, imágenes)
    │   └── seguros/
    │       ├── css/
    │       │   └── style.css           # Estilos personalizados (modo claro, HSL, fuentes, animaciones)
    │       └── js/
    │           └── main.js             # Código interactivo (scroll de cabecera y cierre de toasts)
    │
    └── templates/                      # Plantillas HTML procesadas por el motor de templates de Django
        └── seguros/
            ├── base.html               # Plantilla global con navbar, footer, iconos Lucide y alertas flotantes
            ├── home.html               # Página de inicio con el catálogo de seguros, buscador y filtros
            ├── detail.html             # Página descriptiva del seguro, coberturas y llamados a la acción (CTA)
            ├── login.html              # Pantalla de inicio de sesión para clientes registrados
            ├── register.html           # Pantalla de registro de nuevos clientes
            ├── contract.html           # Pantalla final de contratación con checkout de pago simulado interactivo
            └── dashboard.html          # Panel del cliente donde visualiza sus seguros activos contratados
```

---

## Instrucciones de Instalación y Ejecución

Sigue estos pasos en tu terminal dentro de la carpeta `Frontal seguros` para poner en marcha el proyecto:

1. **Activar el entorno virtual**:
   * En Windows (PowerShell):
     ```powershell
     .venv\Scripts\Activate.ps1
     ```
   * En macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Ejecutar migraciones** (si clonas el proyecto sin base de datos):
   ```bash
   python manage.py migrate
   ```

4. **Poblar datos iniciales** (seguros por defecto):
   ```bash
   python manage.py seed_data
   ```

5. **Iniciar el servidor local**:
   ```bash
   python manage.py runserver
   ```

6. **Explorar el portal**:
   * Abre tu navegador e ingresa a: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

##  Credenciales Administrador

Puedes ingresar al backend administrativo de Django para gestionar los seguros, usuarios y contratos:
* **URL de acceso**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
* **Usuario**: `admin`
* **Contraseña**: `admin123`

---

##  Pruebas Unitarias

Para validar que el sistema funciona correctamente, ejecuta el siguiente comando:
```bash
python manage.py test seguros
```
Esto correrá las 8 pruebas integradas que evalúan la carga de vistas, el registro de clientes, el flujo de login y el proceso completo de contratación de pólizas.
