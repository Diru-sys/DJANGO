from django.shortcuts import render
from .models import Post

#VIEWS
def principal(request):
    posts = Post.objects.filter(titulo__icontains="th")
    print(posts)
    return render(request, "blog/index.html")

def ji(request):
    return render(request, "blog/ji.html")
