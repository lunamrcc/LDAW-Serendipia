from .models import Clases
from django import forms

class ClassForm(forms.ModelForm):
    class Meta:
        model = Clases
        fields = ('nombre', 'descripcion', 'horario', 'requisitos', 'estudiantes')