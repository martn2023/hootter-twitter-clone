# views.py

from django.shortcuts import render

def home(request):
    if request.user.is_authenticated:
        # If user is authenticated, render the authenticated home template
        return render(request, 'core/home_authenticated.html')
    else:
        # If user is not authenticated, render the unauthenticated home template
        return render(request, 'core/home_unauthenticated.html')
