from django.db import models

class Cliente(models.Model):
  nombre = models.CharField(max_length=100)
  direccion = models.CharField(max_length=200)
  ciudad = models.CharField(max_length=100)
  pais = models.CharField(max_length=100)

  class Meta:
    db_table = 'clientes'
  def __str__(self):
    return self.nombre

class Producto(models.Model):
  nombre = models.CharField(max_length=80)
  descripcion = models.TextField()
  precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

  class Meta:
    db_table = 'productos'
  def __str__(self):
    return self.nombre

class Pedido(models.Model):
  cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
  producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
  fecha_creacion = models.DateTimeField(auto_now_add=True)
  cantidad = models.PositiveIntegerField()
  estado = models.CharField(max_length=100)

  class Meta:
    db_table = 'pedidos'
