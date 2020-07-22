from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm


def index(request):
    return render(request, 'app/main.html')


def contacts(request):
    return render(request, 'app/basic.html', {'values': ['Vitaly Sem', 'Skype: dj_skynet', 'Telegram: @vir2s']})


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'New Account created: {username}')

            login(request, user)
            messages.info(request, f'You are now logged in as {username}')

            return redirect('app:index')

        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}: {form.error_messages[msg]}')

    form = NewUserForm
    return render(request, 'app/register.html', context={'form': form})


def logout_request(request):
    logout(request)
    messages.info(request, 'You are logged out successfully')
    return redirect('app:index')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user = authenticate(username=username, password=password, first_name=first_name, last_name=last_name)

            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}')
                return redirect('app:index')

            else:
                messages.error(request, 'Invalid username or password')

        else:
            messages.error(request, 'Invalid username or password')

    form = AuthenticationForm()
    return render(request, 'app/login.html', context={'form': form})
