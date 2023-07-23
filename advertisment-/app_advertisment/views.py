from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'index.html')

def advert(request):
    return render(request, 'advertisement.html')

def advert_post(request):
    return render(request, 'advertisement-post.html')

def login(request):
    return render(request, 'login.html')

def profile(request):
    return render(request, 'profile.html')

def register(request):
    return render(request, 'register.html')

def top(request):
    return render(request, 'top-sellers.html')