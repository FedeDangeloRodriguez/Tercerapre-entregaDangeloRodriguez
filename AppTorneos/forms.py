from django import forms

class EquipoFormulario(forms.Form):

    nombre = forms.CharField(max_length=30 ,required=True)
    barrio = forms.CharField(max_length=30 ,required=True)
    titulos = forms.IntegerField(required=True)

class JugadorFormulario(forms.Form):

    nombre = forms.CharField(max_length=30 ,required=True)
    apellido = forms.CharField(max_length=30 ,required=True)
    edad = forms.IntegerField(required=True)

class EntrenadoresFormulario(forms.Form):

    nombre = forms.CharField(max_length=30 ,required=True)
    apellido = forms.CharField(max_length=30 ,required=True)
    titulos = forms.IntegerField(required=True)
    edad = forms.IntegerField(required=True)
    