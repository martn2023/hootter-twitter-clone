# user_management/urls.py

from django.urls import path
from . import views

app_name = 'user_management'

urlpatterns = [
    path('register/', views.register_new_user, name='register'),
    # Add other paths as needed
]
