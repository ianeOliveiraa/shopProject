from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .forms import ClienteForm, ProdutoForm, VendaForm
from .models import Cliente, Produto, Venda


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

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos.html', {'produtos': produtos})
def home(request):
    return render(request, 'home.html')

# Editar produto
def editar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')  # Nome da view que lista os produtos
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'editar_produto.html', {'form': form})

# Excluir produto
def excluir_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')  # Nome da view que lista os produtos
    return render(request, 'confirmar_exclusao.html', {'produto': produto})




def venda_list(request):
    venda_list = Venda.objects.all()
    paginator = Paginator(venda_list, 5)  # Define 5 clientes por página
    page_number = request.GET.get('page')  # Obtém o número da página atual da URL
    vendas = paginator.get_page(page_number)
    return render(request, 'venda.html', {'vendas': vendas})



def venda_form(request, id=None):
    venda = get_object_or_404(Venda, id=id) if id else None
    if request.method == 'POST':
        form = VendaForm(request.POST, instance=venda)
        if form.is_valid():
            form.save()
            return redirect('venda_list')
    else:
        form = VendaForm(instance=venda)
    return render(request, 'venda_form.html', {'form': form})
