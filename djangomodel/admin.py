from django.contrib import admin

# Register your models here.
from .models import Cliente, Pedido, Producto

admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Producto)