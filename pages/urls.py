from django.urls import path
from .views import AboutView, GalleryView, ExhibitionView, ContactView, AvailableArtView, JournalView

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('exhibition/', ExhibitionView.as_view(), name='exhibition'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('available-art/', AvailableArtView.as_view(), name='available_art'),
    path('journal/', JournalView.as_view(), name='journal'),
]
