from django.shortcuts import render
from .models import Post, Autor, Categoria

#VIEWS
def principal(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "blog/index.html", context)

def detalles(request, pk):
    posts = Post.objects.get(id=pk)
    context = {"posts": posts}
    return render(request, "blog/detalles.html", context)

def autores(request):
    autores = Autor.objects.all()
    context = {"autores": autores}
    return render(request, "blog/autores.html", context)

def categorias(request):
    categorias = Categoria.objects.all()
    context = {"categorias": categorias}
    return render(request, "blog/categorias.html", context)

def entradasAutor(request, pk):
    autor = Autor.objects.get(id=pk)
    posts = Post.objects.filter(autor=pk)
    context = {"posts": posts, "autor": autor}
    return render(request, "blog/entradasAutor.html", context)