from .models import Usuarios
from django import forms

class PasswordInput(forms.PasswordInput):
    input_type = 'password'

class UsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ('Nombre', 'Apaterno', 'Amaterno', 'Telefono', 'Email', 'Passwd')

class LoginForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        Passwd = forms.CharField(widget=forms.PasswordInput)
        fields = ('Email', 'Passwd')
        widgets = {
            'Passwd': PasswordInput()
        }
