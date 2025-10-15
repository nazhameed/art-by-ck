from django.shortcuts import render
from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = "about.html"

class GalleryView(TemplateView):
    template_name = "gallery.html"

class ImmersiveView(TemplateView):
    template_name = "immersive.html"

class ContactView(TemplateView):
    template_name = "contact.html"

class AvailableArtView(TemplateView):
    template_name = "available_art.html"

# Create your views here.
