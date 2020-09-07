from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('<int:blog_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('newblog/', views.blogpost, name='newblog'),
    path('comment/update/<int:pk>', views.comment_update, name='comment_update'),
    path('comment/delete/<int:pk>', views.comment_delete, name='comment_delete'),
]