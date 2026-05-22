from django.contrib import admin
from .models import Marca, Categoria, Vendedor, Tenis, Cliente, Venta, Material

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Vendedor)
admin.site.register(Tenis)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(Material) # <-- Clave para agregar materiales desde el panel admin