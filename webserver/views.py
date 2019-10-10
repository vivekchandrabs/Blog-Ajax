from django.shortcuts import render

# Create your views here.

def signup(request):
    return render(request, "signup.html")

def blogpage(request):
    return render(request, "blogpage.html")

def blogdetail(request):
    return render(request, "blogdetail.html")
