# user_management/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import ExtendedUserCreationForm

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
