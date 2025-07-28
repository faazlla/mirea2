from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def blog1(request):
    return render(request, 'blog1.html', {})

def blog2(request):
    return render(request, 'blog2.html', {})

def blog3(request):
    return render(request, 'blog3.html', {})

def blog4(request):
    return render(request, 'blog4.html', {})

def services(request):
    return render(request, 'services.html', {})