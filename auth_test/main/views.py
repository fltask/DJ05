from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def index(request):
    return render(request, 'main/index.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('main:profile')
        else:
            messages.error(request, 'Ошибка при регистрации. Проверьте введенные данные.')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'main/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, f'Добро пожаловать, {form.get_user().username}!')
            return redirect('main:profile')
        else:
            messages.error(request, 'Неверный логин/email или пароль.')
    else:
        form = CustomAuthenticationForm()
    
    return render(request, 'main/login.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'main/profile.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'Вы вышли из системы.')
    return redirect('main:index')
