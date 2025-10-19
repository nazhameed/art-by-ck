from django import forms
from .models import ContactSubmission

try:
    from crispy_forms.helper import FormHelper
    from crispy_forms.layout import Layout, Submit, Row, Column, Field, Div
    from crispy_forms.bootstrap import Alert, InlineRadios
    CRISPY_AVAILABLE = True
except ImportError:
    CRISPY_AVAILABLE = False


class ContactSubmissionForm(forms.ModelForm):
    """
    Django form for handling all contact requests from website visitors.
    Enhanced with crispy-forms for better styling and layout.
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Add form-control class to all fields for Bootstrap styling
        for field_name, field in self.fields.items():
            if not field.widget.attrs.get('class'):
                field.widget.attrs['class'] = 'form-control'
        
        # Set up crispy forms helper if available
        if CRISPY_AVAILABLE:
            self.helper = FormHelper()
            self.helper.form_method = 'post'
            self.helper.form_class = 'needs-validation'
            self.helper.attrs = {'novalidate': ''}
            
            self.helper.layout = Layout(
                Row(
                    Column('name', css_class='form-group col-md-6 mb-3'),
                    Column('email', css_class='form-group col-md-6 mb-3'),
                    css_class='form-row'
                ),
                Row(
                    Column('phone', css_class='form-group col-md-6 mb-3'),
                    Column('preferred_contact_method', css_class='form-group col-md-6 mb-3'),
                    css_class='form-row'
                ),
                Row(
                    Column('inquiry_type', css_class='form-group col-md-6 mb-3'),
                    Column('subject', css_class='form-group col-md-6 mb-3'),
                    css_class='form-row'
                ),
                Field('message', css_class='form-group mb-3'),
                Div(
                    Row(
                        Column('artwork_title', css_class='form-group col-md-6 mb-3'),
                        Column('artwork_reference', css_class='form-group col-md-6 mb-3'),
                        css_class='form-row'
                    ),
                    css_class='artwork-fields',
                    css_id='artwork-fields'
                ),
                Submit('submit', 'Send Message', css_class='artistic-submit mt-4')
            )
    
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
            'message': forms.Textarea(attrs={'rows': 6, 'placeholder': 'Please provide details about your inquiry...'}),
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your.email@example.com'}),
            'phone': forms.TextInput(attrs={'placeholder': '+46 70 123 45 67'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Brief subject of your inquiry'}),
            'artwork_title': forms.TextInput(attrs={'placeholder': 'Title of the artwork (if applicable)'}),
            'artwork_reference': forms.TextInput(attrs={'placeholder': 'Artwork ID or reference number'}),
        }
        labels = {
            'name': 'Full Name *',
            'email': 'Email Address *',
            'phone': 'Phone Number',
            'inquiry_type': 'Type of Inquiry *',
            'subject': 'Subject *',
            'message': 'Message *',
            'artwork_title': 'Artwork Title',
            'artwork_reference': 'Artwork Reference',
            'preferred_contact_method': 'Preferred Contact Method *',
        }
        help_texts = {
            'name': '',  # Hide the 'Full name' helper text
        }
