from django.shortcuts import render, get_object_or_404
from .models import Tenis

def home(request):
    busqueda = request.GET.get('buscar')
    if busqueda:
        lista_tenis = Tenis.objects.filter(modelo__icontains=busqueda)
    else:
        lista_tenis = Tenis.objects.all()
    return render(request, 'catalogo/index.html', {'lista_tenis': lista_tenis, 'busqueda': busqueda})

def detalle(request, tenis_id):
    # Traemos el par de tenis y Django automáticamente incluirá sus materiales mapeados
    tenis = get_object_or_404(Tenis, pk=tenis_id)
    return render(request, 'catalogo/detalle_tenis.html', {'tenis': tenis})