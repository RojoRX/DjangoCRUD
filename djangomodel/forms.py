from django import forms
from .models import Cliente, Pedido, Producto

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente', 'producto', 'cantidad', 'estado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cliente'].widget = forms.Select(choices=Cliente.objects.all().values_list('id', 'nombre'))
        self.fields['producto'].widget = forms.Select(choices=Producto.objects.all().values_list('id', 'nombre'))

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'direccion', 'ciudad', 'pais']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio_unitario']