from django.db import migrations, models
from djangomodel.models import Cliente, Producto  # Asegúrate de reemplazar 'your_app' con el nombre de tu aplicación


def insertar_clientes(apps, schema_editor):
    Cliente = apps.get_model('djangomodel', 'Cliente')  # Reemplaza 'your_app' con el nombre de tu aplicación
    clientes = [
        Cliente(nombre='Juan Pérez', direccion='Calle 123, número 456', ciudad='Ciudad de México', pais='México'),
        Cliente(nombre='María García', direccion='Avenida Insurgentes, número 789', ciudad='Monterrey', pais='México'),
        Cliente(nombre='Pedro López', direccion='Calle Bolívar, número 101', ciudad='Buenos Aires', pais='Argentina'),
        Cliente(nombre='Sofía Rodríguez', direccion='Avenida Paulista, número 1234', ciudad='São Paulo', pais='Brasil'),
        Cliente(nombre='Ana Smith', direccion='123 Main Street', ciudad='New York', pais='Estados Unidos'),
    ]

    for cliente in clientes:
        cliente.save()

def insertar_productos(apps, schema_editor):
    Producto = apps.get_model('djangomodel', 'Producto')  # Reemplaza 'your_app' con el nombre de tu aplicación
    productos = [
        Producto(nombre='Televisor LED de 55 pulgadas', descripcion='Televisor con resolución 4K Ultra HD, HDR y Smart TV', precio_unitario=15000),
        Producto(nombre='Refrigerador de dos puertas', descripcion='Refrigerador con capacidad de 20 pies cúbicos', precio_unitario=10000),
        Producto(nombre='Lavadora automática de carga frontal', descripcion='Lavadora con capacidad de 15 kilos', precio_unitario=8000),
        Producto(nombre='Celular inteligente', descripcion='Celular con pantalla de 6.7 pulgadas, cámara de 108 megapíxeles y procesador Snapdragon 8 Gen 1', precio_unitario=20000),
        Producto(nombre='Computadora portátil', descripcion='Computadora con pantalla de 15 pulgadas, procesador Intel Core i7 y 16 GB de RAM', precio_unitario=30000),
    ]

    for producto in productos:
        producto.save()

class Migration(migrations.Migration):

    dependencies = [
        ('djangomodel', '0006_pedido_cantidad_pedido_estado'),
    ]
    operations = [
        migrations.RunPython(insertar_clientes),
        migrations.RunPython(insertar_productos),
    ]