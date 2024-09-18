from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseNotAllowed
from .forms import LoginForm,UserRegistrationForm
from .models import Libros
from django.contrib import messages
# Create your views here.
#Funciones de envio de datos al formularios de inicio_sesion y registro
def user_login(request):
    if request.method=='POST':
        form= LoginForm(request.POST)
        if form.is_valid():
            cd= form.cleaned_data
            user= authenticate(request,
                               username=cd['username'],
                               password=cd['password']) #None
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return HttpResponse('Usuario existe')
                else:
                    return HttpResponse('Usuario no identificado')
            else:
                HttpResponse('La informacion no es correcta')
    else:
        form=LoginForm()
        return render(request,'account/login.html',{'form':form})


@login_required
def dashboard(request):
    libros=Libros.objects.all()
    return render(request, 
                  'account/dashboard.html', {'libros':libros})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 
                      'account/register.html',
                      {'user_form': user_form})

#registrar, eliminar, editar y guardar libros

def registrarLibro(request):
    if request.method == 'POST':
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        autor = request.POST['txtAutor']

        libro = Libros.objects.create(codigo=codigo, nombre=nombre, autor=autor)
        messages.success(request, 'Libro registrado exitosamente.')
        return redirect('dashboard')  # Cambia esto si es necesario
    else:
        return HttpResponseNotAllowed(['POST'])

@login_required
def edicionLibro(request, codigo):
    libro = get_object_or_404(Libros, codigo=codigo)
    return render(request, "edicionLibro.html", {'libro': libro})

@login_required
def editarLibro(request):
    if request.method == 'POST':
        codigo = request.POST['txtCodigo']
        nombre = request.POST['txtNombre']
        autor = request.POST['txtAutor']

        libro = get_object_or_404(Libros, codigo=codigo)
        libro.nombre = nombre
        libro.autor = autor
        libro.save()
        messages.success(request, 'Libro actualizado exitosamente.')
        return redirect('dashboard')
    else:
        return redirect('dashboard')  # Redirigir si no es un POST


def eliminarLibro(request,codigo):
    libro=Libros.objects.get( codigo=codigo)
    libro.delete()
    return redirect('dashboard')