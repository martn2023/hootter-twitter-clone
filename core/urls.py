from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_unauthenticated, name='home_unauthenticated'),
]
