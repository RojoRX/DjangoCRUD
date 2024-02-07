from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente, Producto, Pedido
from .forms import PedidoForm, ProductoForm  # Necesitarás crear este formulario

def pedido_list(request):
    pedidos = Pedido.objects.all()
    return render(request, 'pedido_list.html', {'pedidos': pedidos})

def pedido_detail(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    return render(request, 'pedido_detail.html', {'pedido': pedido})

def pedido_new(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.save()
            return redirect('pedido_detail', pk=pedido.pk)
    else:
        form = PedidoForm()
    return render(request, 'pedido_edit.html', {'form': form})

def pedido_edit(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    if request.method == "POST":
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.save()
            return redirect('pedido_detail', pk=pedido.pk)
    else:
        form = PedidoForm(instance=pedido)
    return render(request, 'pedido_edit.html', {'form': form})

def pedido_delete(request, pk):
    pedido = get_object_or_404(Pedido, pk=pk)
    pedido.delete()
    return redirect('pedido_list')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente_list.html', {'clientes': clientes})

def cliente_detail(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'cliente_detail.html', {'cliente': cliente})

def cliente_new(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('cliente_detail', pk=cliente.pk)
    else:
        form = ClienteForm()
    return render(request, 'cliente_edit.html', {'form': form})

def cliente_edit(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.save()
            return redirect('cliente_detail', pk=cliente.pk)
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente_edit.html', {'form': form})

def cliente_delete(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('cliente_list')

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'producto_list.html', {'productos': productos})

def producto_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'producto_detail.html', {'producto': producto})

def producto_new(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('producto_detail', pk=producto.pk)
    else:
        form = ProductoForm()
    return render(request, 'producto_edit.html', {'form': form})

def producto_edit(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('producto_detail', pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto_edit.html', {'form': form})

def producto_delete(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('producto_list')
