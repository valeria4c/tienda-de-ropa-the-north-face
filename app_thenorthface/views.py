from django.shortcuts import render
from .models import Categoria

def tienda(request):
    categorias = Categoria.objects.prefetch_related('productos')
    return render(request, 'tienda.html', {
        'categorias': categorias
    })