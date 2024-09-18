from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Incluye las URLs de autenticación de Django
    path('accounts/', include('django.contrib.auth.urls')),  # Cambia la raíz a 'accounts/'
    
    # Ruta para el dashboard
    path('', views.dashboard, name='dashboard'),
    
    # Ruta para el registro de usuarios
    path('register/', views.register, name='register'),
    
    # Ruta para registrar un libro
    path('registrarLibro/', views.registrarLibro, name='registrar_libro'),  # Agrega un nombre
    
    # Ruta para la edición del libro (GET)
    path('edicionLibro/<str:codigo>/', views.edicionLibro, name='edicion_libro'),  # Agrega un nombre y especifica el tipo
    
    # Ruta para editar libro (POST)
    path('editarLibro/', views.editarLibro, name='editar_libro_post'),  # Cambia el nombre para mayor claridad
    
    # Ruta para eliminar el libro
    path('eliminarLibro/<str:codigo>/', views.eliminarLibro, name='eliminar_libro')  # Agrega un nombre y especifica el tipo
]

