from django.urls import path
from . import views
from pages.views import ExhibitionView

urlpatterns = [
    path('', views.artist_dashboard, name='artist_dashboard'),
    path('gallery/add/', views.gallery_add, name='gallery_add'),
    path('gallery/<int:pk>/edit/', views.gallery_edit, name='gallery_edit'),
    path('gallery/<int:pk>/delete/', views.gallery_delete, name='gallery_delete'),
    path('available-art/add/', views.available_art_add, name='available_art_add'),
    path('available-art/<int:pk>/edit/', views.available_art_edit, name='available_art_edit'),
    path('available-art/<int:pk>/delete/', views.available_art_delete, name='available_art_delete'),
    path('journal/add/', views.journal_add, name='journal_add'),
    path('journal/<int:pk>/edit/', views.journal_edit, name='journal_edit'),
    path('journal/<int:pk>/delete/', views.journal_delete, name='journal_delete'),
    path('exhibition/', ExhibitionView.as_view(), name='exhibition'),
]
