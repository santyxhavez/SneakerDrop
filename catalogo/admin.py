from django.contrib import admin
from .models import Marca, Categoria, Vendedor, Tenis, Cliente, Venta

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Vendedor)
admin.site.register(Tenis)
admin.site.register(Cliente)
admin.site.register(Venta)