from django.urls import path
from . import views

app_name = 'public_messages'

urlpatterns = [
    path('create/', views.create_post, name='create_post'),

    path('details/<int:post_id>/', views.post_details, name='post_details'),

    path('mine', views.own_posts, name='see_my_posts'),

    path('everyone_else', views.everyone_elses_posts, name='see_everyone_elses_posts'),

    path('reply/<int:parent_id>/', views.create_post, name='reply_post'),

]