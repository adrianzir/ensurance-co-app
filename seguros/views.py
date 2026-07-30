from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Seguro, Contrato
from .forms import RegistroForm, ContratarForm

def home(request):
    query = request.GET.get('q', '')
    categoria_filter = request.GET.get('categoria', '')
    
    seguros = Seguro.objects.all()
    
    if query:
        seguros = seguros.filter(
            Q(titulo__icontains=query) | 
            Q(descripcion_corta__icontains=query) | 
            Q(descripcion_detallada__icontains=query)
        )
        
    if categoria_filter:
        seguros = seguros.filter(categoria=categoria_filter)
        
    categorias = Seguro.CATEGORIAS
    
    # Destacados para la sección principal (hero o banner)
    destacados = Seguro.objects.filter(destacado=True)[:3]
    if not destacados.exists():
        destacados = seguros[:3]
        
    context = {
        'seguros': seguros,
        'categorias': categorias,
        'destacados': destacados,
        'query': query,
        'categoria_seleccionada': categoria_filter,
    }
    return render(request, 'seguros/home.html', context)

def detalle(request, seguro_id):
    seguro = get_object_or_404(Seguro, pk=seguro_id)
    # Recomendados (otros seguros de la misma categoría o destacados)
    recomendados = Seguro.objects.filter(categoria=seguro.categoria).exclude(pk=seguro.id)[:3]
    if not recomendados.exists():
        recomendados = Seguro.objects.exclude(pk=seguro.id)[:3]
        
    context = {
        'seguro': seguro,
        'recomendados': recomendados,
    }
    return render(request, 'seguros/detail.html', context)

def registro_usuario(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"¡Registro exitoso! Bienvenido, {user.first_name}.")
            return redirect('dashboard')
        else:
            messages.error(request, "Por favor corrige los errores a continuación.")
    else:
        form = RegistroForm()
        
    return render(request, 'seguros/register.html', {'form': form})

def login_usuario(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"¡Hola de nuevo, {user.first_name or user.username}!")
                next_url = request.GET.get('next', 'dashboard')
                return redirect(next_url)
        messages.error(request, "Nombre de usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
        
    return render(request, 'seguros/login.html', {'form': form})

def logout_usuario(request):
    logout(request)
    messages.info(request, "Has cerrado sesión correctamente.")
    return redirect('home')

@login_required
def contratar_seguro(request, seguro_id):
    seguro = get_object_or_404(Seguro, pk=seguro_id)
    
    # Verificar si el usuario ya tiene este seguro contratado y activo
    ya_contratado = Contrato.objects.filter(usuario=request.user, seguro=seguro, estado='ACTIVO').exists()
    if ya_contratado:
        messages.warning(request, f"Ya tienes contratado el seguro '{seguro.titulo}' de forma activa.")
        return redirect('dashboard')
        
    if request.method == 'POST':
        form = ContratarForm(request.POST)
        if form.is_valid():
            contrato = form.save(commit=False)
            contrato.usuario = request.user
            contrato.seguro = seguro
            contrato.precio_pactado = seguro.precio_mensual
            contrato.estado = 'ACTIVO'
            contrato.save()
            messages.success(request, f"¡Felicitaciones! Has contratado exitosamente el '{seguro.titulo}'.")
            return redirect('dashboard')
    else:
        form = ContratarForm()
        
    context = {
        'seguro': seguro,
        'form': form,
    }
    return render(request, 'seguros/contract.html', context)

@login_required
def dashboard(request):
    contratos = Contrato.objects.filter(usuario=request.user).order_by('-fecha_contratacion')
    context = {
        'contratos': contratos,
    }
    return render(request, 'seguros/dashboard.html', context)

