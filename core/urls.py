from django.urls import path,include
from .views import *

urlpatterns = [
    
    path('', EstudianteListView.as_view() , name="home"),
    path('<int:pk>/', EstudianteDetailView.as_view(), name='ver'),
    path('agregar/', EstudianteCreateView.as_view() , name="agregar"),
    path('<int:pk>/editar/', EstudianteUpdateView.as_view() , name="editar"),
    path('<int:pk>/delete/', EstudianteDeleteView.as_view() , name="eliminar"),

]
