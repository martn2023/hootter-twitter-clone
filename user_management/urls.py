# user_management/urls.py

from django.urls import path
from . import views

app_name = 'user_management'

urlpatterns = [
    path('register/', views.register_new_user, name='register_new_user'),
    path('login/', views.login_start, name='login_start'),
    path('logout/', views.logout_user, name='logout'),
    path('<int:user_id>/', views.ExtendedUserProfileDetails, name='user_details'),
    path('edit/', views.profile_edit, name='profile_edit'),
    path('users/', views.list_users, name='list_users'),
    path('readers/', views.list_readers, name='list_readers'),
    path('posters/', views.list_posters, name='list_posters'),
    path('user_categories/', views.list_user_categories, name='user_categories'),


    path('follow/<int:user_id>/', views.follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', views.unfollow_user, name='unfollow_user'),

    path('following/', views.following_list, name='following_list')

]
