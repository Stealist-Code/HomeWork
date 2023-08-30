from django.shortcuts import render
from django.http import HttpResponse

from .models import Advertisment

# Create your views here.
def index(request):
    advertisement = Advertisment.objects.all()
    context = {'advertisement':advertisement}
    return render(request,'index.html',context=context)

def top(request):
    return render(request,'top-sellers.html')


def advertisement_post(request):
    return render(request,'advertisement-post.html')


def advertisement(request):
    return render(request,'advertisement.html')

def login(request):
    return render(request,'login.html')

def profile(request):
    return render(request,'profile.html')

def register(request):
    return render(request,'register.html')