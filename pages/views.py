from django.shortcuts import render
from django.views.generic import TemplateView
from dashboard.models import GalleryImage, AvailableArt, JournalEntry, About, Exhibition
from cloudinary import CloudinaryVideo
from cloudinary.utils import cloudinary_url


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
        exhibitions = Exhibition.objects.all().order_by('-date')

        # Generate video URLs with adaptive bitrate streaming (HLS)
        for exhibition in exhibitions:
            if exhibition.video and exhibition.video.public_id:
                public_id = exhibition.video.public_id

                # Generate HLS URL for adaptive bitrate streaming
                exhibition.video_hls_url = CloudinaryVideo(public_id).build_url(
                    resource_type='video',
                    streaming_profile='auto',
                    format='m3u8'
                )

                # Generate MP4 URL as fallback
                exhibition.video_mp4_url = CloudinaryVideo(public_id).build_url(
                    resource_type='video',
                    quality='auto'
                )

                # Generate poster image
                exhibition.video_poster_url = cloudinary_url(
                    public_id,
                    resource_type='video',
                    format='jpg',
                    quality='auto',
                    fetch_format='auto'
                )[0]

        context['exhibitions'] = exhibitions
        return context


class ContactView(TemplateView):
    template_name = "contact.html"


class AvailableArtView(TemplateView):
    template_name = "available_art.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['available_arts'] = AvailableArt.objects.filter(
            is_available=True).order_by('-created_at')
        return context


class JournalView(TemplateView):
    template_name = "journal.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['journal_entries'] = JournalEntry.objects.all().order_by(
            '-created_at')
        return context

# Create your views here.
