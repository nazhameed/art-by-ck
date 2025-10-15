from django.urls import path
from .views import AboutView, GalleryView, ImmersiveView, ContactView, AvailableArtView

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('immersive/', ImmersiveView.as_view(), name='immersive'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('available-art/', AvailableArtView.as_view(), name='available_art'),
]
