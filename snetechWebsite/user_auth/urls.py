from django.contrib import admin
from django.urls import path,include
from user_auth import views

app_name = 'user_auth'
urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('authenticate_user/', views.authenticate_user,name='authenticate_user')
]