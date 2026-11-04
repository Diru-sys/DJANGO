from django.shortcuts import render
from .models import Post, Autor

#VIEWS
def principal(request):
    posts = Post.objects.all()
    context = {"posts": posts
            }
    return render(request, "blog/index.html", context)

def detalles(request, pk):
    post= Post.objects.get(id=pk)
    return render(request, "blog/detalles.html", {"post": post})

def autores(request):
    autores = Autor.objects.all()
    context = {"autores": autores}
    return render(request, "blog/autores.html", context)

def entradasAutor(request, pk):
    posts = Post.objects.filter(autor_id=pk)
    return render(request, "blog/entradasAutor.html", {"posts": posts})