# user_management/urls.py

from django.urls import path
from . import views

app_name = 'user_management'

urlpatterns = [
    path('register/', views.register_new_user, name='register_new_user'),
    path('login/', views.login_start, name='login_start'),
    path('logout/', views.logout_user, name='logout'),
    path('<int:user_id>/', views.ExtendedUserProfileDetails, name='user_details')
]
