from django import forms
from .models import Contacto, Productos, Categorias
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class ConctactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        widgets={
            'mensaje': forms.Textarea(attrs={
                'rows':5,
                'cols':30
                }),
        }
        fields = '__all__'

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Productos
        fields = ["nombre", "descripcion", "precio", "stock", "categoria", "oferta", "imagen"]

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categorias
        fields = ["nombre"]

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "first_name","last_name","email","password1","password2"]


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
