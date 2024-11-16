from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import ClienteForm, ProdutoForm
from .models import Cliente, Produto


def cliente_list(request):
    clientes_list = Cliente.objects.all()
    paginator = Paginator(clientes_list, 5)  # Define 5 clientes por página
    page_number = request.GET.get('page')  # Obtém o número da página atual da URL
    clientes = paginator.get_page(page_number)
    return render(request, 'clientes.html', {'clientes': clientes})


def cliente_form(request, id=None):
    cliente = get_object_or_404(Cliente, id=id) if id else None
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cliente_form.html', {'form': form})


def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})


def produto_form(request, id=None):
    produto = get_object_or_404(Produto, id=id) if id else None
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('produto_list')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produto_form.html', {'form': form})

def cadastro_produto(request):
    return produto_form(request)

def produto_list(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})

def home(request):
    return render(request, 'home.html')


