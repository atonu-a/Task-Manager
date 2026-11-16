from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name=""), name="login"),
    path('create/', views.create_task, name="create"),
    path('tasks/<str:title>/', views.task_details, name="details"),
    path('delete/<str:title>/', views.delete_task, name="delete"),
    path('edit/<str:title>/', views.edit_task, name="edit"),
    path('<str:title>/mark-as-complete/', views.mark_as_completed, name="mark_as_completed"),
    
    
]
