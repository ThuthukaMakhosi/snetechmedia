from django.urls import path, include
from . import views

app_name = 'snetech'
urlpatterns = [
path('', views.home, name = 'home'),
path('artists', views.artists, name = 'artists'),
path('gallery', views.gallery, name = 'gallery'),
path('contact', views.contact, name = 'contact'),
]