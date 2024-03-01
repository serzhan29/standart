from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer


def serzhan(request):
    return render(request, 'user/serzhan.html')


def home(request):
    return render(request, 'salary/employee_list.html')


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
                return redirect('salary/employees')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

