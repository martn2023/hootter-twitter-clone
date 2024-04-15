from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth.models import User

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


def ExtendedUserProfileDetails(request, user_id):
    if not request.user.is_authenticated:
        return redirect('user_management:login_start')

    user = get_object_or_404(User, pk=user_id)
    try:
        profile = user.extended_profile
    except ExtendedUserProfile.DoesNotExist:
        return HttpResponse("The user's profile does not exist.", status=404)

    return render(request, 'user_management/user_profile_view.html', {'user_profile': profile})