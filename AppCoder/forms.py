from django import forms

class AddAbuelos(forms.Form):
    nombre=forms.CharField(label="Nombre")
    paisDeNac=forms.CharField(label="Páis de nacimiento")
    anioDeNac=forms.IntegerField(label="Año de nacimiento")

class AddPadres(forms.Form):
    nombre=forms.CharField(label="Nombre")
    paisDeNac=forms.CharField(label="Páis de nacimiento")
    anioDeNac=forms.IntegerField(label="Año de nacimiento")