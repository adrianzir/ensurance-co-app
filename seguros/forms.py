from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Contrato
import datetime

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")
    first_name = forms.CharField(max_length=30, required=True, label="Nombre")
    last_name = forms.CharField(max_length=30, required=True, label="Apellido")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user


class ContratarForm(forms.ModelForm):
    fecha_inicio = forms.DateField(
        label="Fecha de Inicio de Cobertura",
        initial=datetime.date.today,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'min': datetime.date.today().strftime('%Y-%m-%d'),
            'class': 'form-input'
        })
    )

    class Meta:
        model = Contrato
        fields = ['fecha_inicio']
