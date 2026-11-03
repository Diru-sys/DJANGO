from django.shortcuts import render
from .models import Post

#VIEWS
def principal(request):
    posts = Post.objects.all()
    context = {"posts": posts
            }
    return render(request, "blog/index.html", context)

def ji(request):
    return render(request, "blog/ji.html")

def detalles(request, pk):
    post= Post.objects.get(id=pk)
    return render(request, "blog/detalles.html", {"post": post})