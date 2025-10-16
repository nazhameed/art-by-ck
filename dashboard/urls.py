from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_dashboard, name='artist_dashboard'),
]
