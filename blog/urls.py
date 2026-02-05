from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
 # Homepage
 path('', views.home_view, name='home'),

 # Create new post
 path('post/create/', views.post_create_view, name='post_create'),

 # View single post - NOTICE: <slug:slug> captures the post slug
 path('post/<slug:slug>/', views.post_detail_view, name='post_detail'),

 # Edit post - NOTICE: <slug:slug> captures the post slug
 path('post/<slug:slug>/edit/', views.post_edit_view, name='post_edit'),

 # Delete post - NOTICE: <slug:slug> captures the post slug
 path('post/<slug:slug>/delete/', views.post_delete_view, name='post_delete'),
]