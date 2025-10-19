from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib import messages
from contactform.forms import ContactSubmissionForm
from contactform.emails import send_contact_notification_email, send_confirmation_email
from django.shortcuts import render
from django.views.generic import TemplateView
from dashboard.models import GalleryImage, AvailableArt, JournalEntry, About, Exhibition
from contactform.forms import ContactSubmissionForm
from cloudinary import CloudinaryVideo
from cloudinary.utils import cloudinary_url


class HomeView(TemplateView):
    template_name = "home.html"


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
        exhibitions_qs = Exhibition.objects.all().order_by('-date')
        exhibitions = list(exhibitions_qs)

        def clean_title(value: str | None) -> str:
            if not value:
                return ""
            return value.replace("[featured]", "").strip()

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

            exhibition.display_title = clean_title(exhibition.title)

        special_feature_title = "Evening Garden Exhibition 2025"
        featured_exhibition = None
        fallback_featured = None

        for exhibition in exhibitions:
            title_value = exhibition.title or ""
            if "[featured]" in title_value:
                featured_exhibition = exhibition
                break
            if fallback_featured is None and clean_title(title_value) == special_feature_title:
                fallback_featured = exhibition

        if featured_exhibition is None:
            featured_exhibition = fallback_featured

        if featured_exhibition:
            remaining_exhibitions = [ex for ex in exhibitions if ex != featured_exhibition]
        else:
            remaining_exhibitions = exhibitions

        context['exhibitions'] = remaining_exhibitions
        context['featured_exhibition'] = featured_exhibition
        return context


class ContactView(View):
    template_name = "contact.html"
    
    def get(self, request):
        """Handle GET requests - display the contact page with form"""
        context = {
            'contact_form': ContactSubmissionForm()
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        """Handle POST requests - process form submission"""
        form = ContactSubmissionForm(request.POST)
        if form.is_valid():
            contact_submission = form.save()
            
            # Send email notifications
            notification_sent = send_contact_notification_email(contact_submission)
            confirmation_sent = send_confirmation_email(contact_submission)
            
            # Create success message based on email sending status
            if notification_sent:
                success_message = (
                    f"Thank you, {contact_submission.name}! Your message has been sent to Cecilia. "
                    f"You should receive a confirmation email shortly, and she'll get back to you via "
                    f"{contact_submission.get_preferred_contact_method_display().lower()} within 24-48 hours."
                )
            else:
                success_message = (
                    f"Thank you, {contact_submission.name}! Your message has been received and saved. "
                    f"We'll get back to you via {contact_submission.get_preferred_contact_method_display().lower()} soon."
                )
            
            # Add success message
            messages.success(request, success_message)
            
            # Redirect to the same page to prevent resubmission
            return redirect('contact')
        else:
            # Form is invalid, show errors
            messages.error(
                request,
                "Please correct the errors below and try again."
            )
            
        # Return the contact page with the form (including any errors)
        context = {
            'contact_form': form
        }
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactSubmissionForm()
        return context


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
