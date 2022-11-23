from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, Template
from .models import *
from .forms import *
from django.urls import reverse_lazy

#imports para login
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from AppLogin.forms import UserRegisterForm,UserEditForm, AvatarForm
from django.contrib.auth.decorators import login_required

def home(request):
   return render(request, "AppLogin/home.html", {"imagen":obtenerAvatar(request)})


def login_request(request):
   if request.method=="POST":
      form=AuthenticationForm(request, data=request.POST)
      if form.is_valid():
         #info=miFormulario.cleaned_data
         usu=request.POST["username"]
         clave=request.POST["password"]
         usuario=authenticate(username=usu,password=clave)
         if usuario is not None:
            login(request,usuario)
            return render(request, 'AppLogin/home.html', {'mensaje':f"Bienvenido {usuario}"})
         else:
            return render(request, 'AppLogin/login.html', {"formulario":form, 'mensaje': 'Usuario o contraseña incorrectos'})
      else:
         return render(request, "AppLogin/login.html", {"formulario":form, 'mensaje': 'Formulario invalido'})
   else:
      form=AuthenticationForm()
      return render(request, "AppLogin/login.html", {"formulario":form})

def register_request(request):
   if request.method=="POST":
      form=UserRegisterForm(request.POST)
      if form.is_valid():
         username=form.cleaned_data["username"]
         form.save()
         return render(request, 'AppLogin/registro.html', {'mensaje':f"Usuario {username} creado, ya puede iniciar sesion"})
   else:
      form=UserRegisterForm()
   return render(request, 'AppLogin/registro.html', {"formulario":form})
   
@login_required(login_url='/AppLogin/login/')
def edicionPerfil(request):
    usuario=request.user
    if request.method=="POST":
        form= UserEditForm(request.POST)
        if form.is_valid():
            usuario.first_name=form.cleaned_data["first_name"]
            usuario.last_name=form.cleaned_data["last_name"]
            usuario.email=form.cleaned_data["email"]
            usuario.password1=form.cleaned_data["password1"]
            usuario.password2=form.cleaned_data["password2"]
            usuario.save()
            return render(request, 'AppLogin/home.html', {'mensaje':f"Perfil de {usuario} editado"})
    else:
        form= UserEditForm(instance=usuario)
    return render(request, 'AppLogin/edicionPerfil.html', {'form':form, 'usuario':usuario})

@login_required(login_url='/AppLogin/login/')
def agregarAvatar(request):
    if request.method == 'POST':
        formulario=AvatarForm(request.POST, request.FILES)
        if formulario.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if(len(avatarViejo)>0):
                avatarViejo.delete()
            avatar=Avatar(user=request.user, imagen=formulario.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'AppLogin/home.html', {'usuario':request.user, 'mensaje':'AVATAR AGREGADO EXITOSAMENTE', "imagen":obtenerAvatar(request)})
    else:
        formulario=AvatarForm()
    return render(request, 'AppLogin/agregarAvatar.html', {'form':formulario, 'usuario':request.user, "imagen":obtenerAvatar(request)})

@login_required(login_url='/AppLogin/login/')
def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen=""
    return imagen

def about(request):
    return render(request, 'AppLogin/about.html')

