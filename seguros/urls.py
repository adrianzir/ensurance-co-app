from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('seguro/<int:seguro_id>/', views.detalle, name='detalle'),
    path('registro/', views.registro_usuario, name='registro'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('contratar/<int:seguro_id>/', views.contratar_seguro, name='contratar'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
