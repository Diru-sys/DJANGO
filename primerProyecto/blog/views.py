from django.shortcuts import render

#VIEWS
def principal(request):
    return render(request, "blog/index.html")
