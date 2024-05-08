from django.urls import path
from . import views

app_name = 'public_messages'

urlpatterns = [
    path('create/', views.create_post, name='create_post'),

    path('mine', views.own_posts, name='see_my_posts'),

    path('reply/<int:parent_id>/', views.create_post, name='reply_post'),

]