from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# View for authenticated users
@login_required(login_url='/login/')  # Redirects to /login/ if not authenticated
def home_authenticated(request):
    return render(request, 'core/home_authenticated.html')

# View for unauthenticated users
def home_unauthenticated(request):
    return render(request, 'core/home_unauthenticated.html')
