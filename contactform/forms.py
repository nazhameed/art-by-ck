from django import forms
from .models import ContactSubmission


class ContactSubmissionForm(forms.ModelForm):
    """
    Django form for handling all contact requests from website visitors.
    """
    
    class Meta:
        model = ContactSubmission
        fields = [
            'name', 
            'email', 
            'phone', 
            'inquiry_type', 
            'subject', 
            'message',
            'artwork_title',
            'artwork_reference',
            'preferred_contact_method'
        ]
        widgets = {
            'message': forms.Textarea(attrs={'rows': 6}),
        }
