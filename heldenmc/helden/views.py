from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Article


def index(request):
    article_list = Article.objects.all()
    return render(request, 'index.html', {'articles': article_list})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['confirm_password']

        if password==password_confirmation:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email is already in use.')
                return redirect('register')
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username is already in use.')
                return redirect('register')
        else:
            user = User.objects.create_user(username=username, email=email, password = password)
            user.save();
            return redirect('login')
    else:
        return render(request, 'register.html')

def donate(request):
    return render(request, 'donate.html')
# try to put article functions inside of a for loop
