from django.shortcuts import render
from django.views.generic import TemplateView
from dashboard.models import GalleryImage, AvailableArt, JournalEntry, About, Exhibition

class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        return context

class GalleryView(TemplateView):
    template_name = "gallery.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = GalleryImage.objects.all().order_by('-created_at')
        return context

class ExhibitionView(TemplateView):
    template_name = "exhibition.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exhibitions'] = Exhibition.objects.all().order_by('-date')
        return context

class ContactView(TemplateView):
    template_name = "contact.html"

class AvailableArtView(TemplateView):
    template_name = "available_art.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['available_arts'] = AvailableArt.objects.filter(is_available=True).order_by('-created_at')
        return context

class JournalView(TemplateView):
    template_name = "journal.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['journal_entries'] = JournalEntry.objects.all().order_by('-created_at')
        return context

# Create your views here.
