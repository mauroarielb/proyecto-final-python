from dataclasses import fields
from django import forms
from .models import *
from .models import Post
from ckeditor.fields import RichTextField

class FormularioPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo','subtitulo', 'imagen', 'contenido']
        help_texts = {k:"" for k in fields}

        
