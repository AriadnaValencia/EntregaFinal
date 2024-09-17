from django import forms
from .models import Blog  # Asegúrate de que el modelo esté bien importado

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
