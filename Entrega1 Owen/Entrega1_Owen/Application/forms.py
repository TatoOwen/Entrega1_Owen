from django import forms

class ProductoForm(forms.Form):
    nombre = forms.CharField(max_length= 25)
    serie = forms.IntegerField()
    tipo = forms.CharField(max_length=10)

class VendedorForm(forms.Form):

    nombre = forms.CharField(max_length= 25)
    apellido = forms.CharField(max_length= 25)
    cuil = forms.IntegerField()
    DNI = forms.IntegerField()

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length= 25)
    apellido = forms.CharField(max_length= 25)
    telefono = forms.IntegerField()