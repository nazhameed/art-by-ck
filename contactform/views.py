from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import JsonResponse
from .forms import ContactSubmissionForm
from .models import ContactSubmission
from .emails import send_contact_notification_email, send_confirmation_email

# Create your views here.

class ContactFormView(CreateView):
    """
    View to handle contact form submissions.
    Displays the form on GET requests and processes submissions on POST requests.
    """
    model = ContactSubmission
    form_class = ContactSubmissionForm
    template_name = 'contactform/contactform.html'
    success_url = reverse_lazy('contactform:contact_success')
    
    def form_valid(self, form):
        """
        Handle valid form submission.
        Save the contact submission, send emails, and show success message.
        """
        contact_submission = form.save()
        
        # Send email notifications
        notification_sent = send_contact_notification_email(contact_submission)
        confirmation_sent = send_confirmation_email(contact_submission)
        
        # Create success message
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
        messages.success(self.request, success_message)
        
        # For AJAX requests, return JSON response
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': f"Thank you, {contact_submission.name}! Your message has been sent.",
                'email_sent': notification_sent
            })
        
        return super().form_valid(form)
    
    def form_invalid(self, form):
        """
        Handle invalid form submission.
        Show error messages and return form with errors.
        """
        messages.error(
            self.request,
            "There were some errors in your submission. Please check the form and try again."
        )
        
        # For AJAX requests, return JSON response with errors
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'errors': form.errors,
                'message': "Please check the form for errors and try again."
            })
        
        return super().form_invalid(form)
