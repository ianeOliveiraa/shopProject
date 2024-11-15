from django.shortcuts import render, redirect
from .models import Cliente, Produto, Venda
from .forms import ClienteForm, ProdutoForm, VendaForm

def cliente_list(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes': clientes})

def cliente_form(request, id=None):
    cliente = Cliente.objects.get(id=id) if id else None
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente_form.html', {'form': form})

# Similar para Produto e Venda
# Funções `produto_list`, `produto_form`, `venda_list`, `venda_form`
from django.shortcuts import render

# Create your views here.
