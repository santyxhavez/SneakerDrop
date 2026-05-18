from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tenis/<int:tenis_id>/', views.detalle, name='detalle'),
]