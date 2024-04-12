from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from .forms import ExtendedUserCreationForm

def login_start(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next')  # Get the next URL from the form
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url:
                return redirect(next_url)  # Redirect to the next URL if provided
            else:
                return redirect('/')  # Redirect to the root URL
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login_start')
    else:
        return render(request, 'user_management/login_start.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def register_new_user(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('some_home_view')  # Redirect to a home page or similar
    else:
        form = ExtendedUserCreationForm()
    return render(request, 'user_management/register_new_user.html', {'form': form})
