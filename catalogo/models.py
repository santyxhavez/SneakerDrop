from django.db import models

class Marca(models.Model):
    nombre = models.CharField(max_length=50) # Ej: Nike, Adidas, Puma
    pais = models.CharField(max_length=50, blank=True)
    def __str__(self): return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50) # Ej: Running, Basketball, Casual
    descripcion = models.TextField(blank=True)
    def __str__(self): return self.nombre

class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    sucursal = models.CharField(max_length=100)
    def __str__(self): return self.nombre

class Tenis(models.Model):
    modelo = models.CharField(max_length=100)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    talla = models.DecimalField(max_digits=4, decimal_places=1) # Ej: 27.5
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='tenis/', null=True, blank=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.SET_NULL, null=True)
    def __str__(self): return f"{self.marca} {self.modelo}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    def __str__(self): return self.nombre

class Venta(models.Model):
    tenis = models.ForeignKey(Tenis, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_compra = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self): return f"Venta: {self.tenis} a {self.cliente}"