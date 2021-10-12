from django import forms
from django.core.exceptions import ValidationError
from django.db.models import fields
from django.forms import ModelForm
from django.forms.fields import IntegerField
from .models import Pelicula
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PeliculaForm(ModelForm):

    nombre = forms.CharField(min_length=2, max_length=200)
    duracion = forms.IntegerField(min_value=5, max_value=500)



    class Meta:
        model = Pelicula
        fields = ['nombre','duracion','año', 'Genero','fecha_estreno','sinopsis','imagen']

        widgets = {
            'fecha_estreno': forms.SelectDateWidget(years=range(1945, 2022))
        }
        
    def clean_fecha_estreno(self):
        fecha = self.cleaned_data['fecha_estreno']
        if fecha > datetime.date.today():
            raise forms.ValidationError("La fecha no puede ser mayor al dia de hoy")
        return fecha

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']