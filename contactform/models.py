from django.db import models
from django.utils import timezone
from django.core.validators import EmailValidator

# Create your models here.

class ContactSubmission(models.Model):
    """
    Model for handling contact form submissions from website visitors.
    Supports numerous types of enquiries, including both general ones and art purchase interest.
    """
    
    INQUIRY_TYPES = [
        ('general', 'General Inquiry'),
        ('purchase', 'Purchase Interest'),
        ('exhibition', 'Exhibition Inquiry'),
        ('other', 'Other'),
    ]
    
    # Basic contact information
    name = models.CharField(max_length=100, help_text="Full name")
    email = models.EmailField(validators=[EmailValidator()], help_text="Email address for response")
    phone = models.CharField(max_length=20, blank=True, null=True, help_text="Optional phone number")
    
    # Inquiry details
    inquiry_type = models.CharField(
        max_length=20, 
        choices=INQUIRY_TYPES, 
        default='general',
        help_text="Type of inquiry"
    )
    subject = models.CharField(max_length=100, help_text="Brief subject of the inquiry")
    message = models.TextField(help_text="Detailed information")
    
    # Art-specific fields (for purchase inquiries)
    artwork_title = models.CharField(
        max_length=100, 
        blank=True, 
        null=True,
        help_text="Title of artwork if inquiry is about a specific piece"
    )
    # PK from artwork model
    artwork_reference = models.CharField(
        max_length=50, 
        blank=True, 
        null=True,
        help_text="Artwork ID or reference number"
    )
    
    # Admin tracking fields
    submitted_at = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False, help_text="Has this inquiry been read?")
    is_responded = models.BooleanField(default=False, help_text="Has this inquiry been responded to?")
    response_notes = models.TextField(
        blank=True, 
        null=True,
        help_text="Internal notes for follow-up"
    )
    
    # Optional fields for better customer service
    preferred_contact_method = models.CharField(
        max_length=10,
        choices=[('email', 'Email'), ('phone', 'Phone'), ('either', 'Either')],
        default='email',
        help_text="Your preferred method of contact"
    )
    
    class Meta:
        ordering = ['-submitted_at']  # Most recent first
        verbose_name = "Contact Requests"
        verbose_name_plural = "Contact Requests"
    
    def __str__(self):
        return f"{self.name} - {self.get_inquiry_type_display()} - {self.submitted_at.strftime('%Y-%m-%d')}"
    
    # Can be used to filter messages that could be expressing interest in a purchase
    @property
    def is_artwork_inquiry(self):
        """Returns True if this is an inquiry about a specific artwork"""
        return bool(self.artwork_title or self.artwork_reference)
