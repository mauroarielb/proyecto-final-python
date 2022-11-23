from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100, unique=True, null=False)
    subtitulo = models.CharField(max_length=100, unique=True, null=False)
    imagen = models.ImageField(upload_to='posts',null=True,blank=True)
    contenido = RichTextField(null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_edicion = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.titulo
     