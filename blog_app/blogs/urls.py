from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('<int:pageId>/', views.blog_detail, name='blog_detail'),
    path('create/', views.create_blog, name='create_blog'),
    path('<int:pageId>/edit/', views.edit_blog, name='edit_blog'),
    path('<int:pageId>/delete/', views.delete_blog, name='delete_blog'),
]
