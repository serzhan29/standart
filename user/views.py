from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm


def home(request):
    return render(request, 'user/home.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Войти успешно, перенаправить на нужную страницу
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})
