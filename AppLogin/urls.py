from django.urls import path

from AppLogin.views import *
from Blogs.views import *
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path('home/',home, name='home'),
    path('login/',login_request, name='login'),
    path('registro/',register_request, name='registro'),
    path('', home),
    path('logout/', LogoutView.as_view(template_name='AppLogin/logout.html'), name='logout'),
    path('edicionPerfil/', edicionPerfil, name='edicionPerfil'),
    path('agregarAvatar/', agregarAvatar, name='agregarAvatar'),
    path('crear_post/', crear_post, name= 'crear_post'),
    path('posteos/', posteos, name= 'posteos'),
    path('eliminar_post/<post_id>', eliminar_post, name="eliminar_post"),
    path('editarPost/<id>', editar_post, name='editarPost'),
    path('verPost/<int:id>', detalle_post, name='verPost'),
    path('about/', about, name='about'),

]