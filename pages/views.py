from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib import messages
from contactform.forms import ContactSubmissionForm

class AboutView(TemplateView):
    template_name = "about.html"

class GalleryView(TemplateView):
    template_name = "gallery.html"

class ImmersiveView(TemplateView):
    template_name = "immersive.html"

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
            
            # Add success message
            messages.success(
                request, 
                f"Thank you, {contact_submission.name}! Your message has been received. "
                f"We'll get back to you via {contact_submission.get_preferred_contact_method_display().lower()} soon."
            )
            
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

class AvailableArtView(TemplateView):
    template_name = "available_art.html"

class JournalView(TemplateView):
    template_name = "journal.html"

# Create your views here.
