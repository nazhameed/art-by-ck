from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def send_contact_notification_email(contact_submission):
    """
    Send email notification to the artist when a new contact form is submitted.
    
    Args:
        contact_submission: ContactSubmission model instance
    
    Returns:
        bool: True if email was sent successfully, False otherwise
    """
    try:
        # Render email templates
        text_content = render_to_string(
            'contactform/emails/contact_notification.txt', 
            {'contact': contact_submission}
        )
        html_content = render_to_string(
            'contactform/emails/contact_notification.html', 
            {'contact': contact_submission}
        )
        
        # Create subject line
        subject = f"New {contact_submission.get_inquiry_type_display()} - {contact_submission.subject}"
        
        # Create and send email
        email = EmailMultiAlternatives(
            subject=subject,
            body=text_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.CONTACT_EMAIL],
            reply_to=[contact_submission.email]  # Allow direct reply to the visitor
        )
        email.attach_alternative(html_content, "text/html")
        
        # Send the email
        email.send()
        
        logger.info(f"Contact notification email sent successfully for submission {contact_submission.id}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to send contact notification email for submission {contact_submission.id}: {str(e)}")
        return False


def send_confirmation_email(contact_submission):
    """
    Send confirmation email to the visitor who submitted the contact form.
    
    Args:
        contact_submission: ContactSubmission model instance
    
    Returns:
        bool: True if email was sent successfully, False otherwise
    """
    try:
        subject = f"Thank you for contacting Art by CK - {contact_submission.subject}"
        
        message = f"""Dear {contact_submission.name},

Thank you for reaching out through my Art by CK website. 

I have received your {contact_submission.get_inquiry_type_display().lower()} regarding "{contact_submission.subject}" and truly appreciate your interest in my work.

NEXT STEPS:
• You will receive my response via {contact_submission.get_preferred_contact_method_display().lower()} as requested
• For purchase inquiries, I will provide detailed artwork information and pricing

I'm excited to connect with you and discuss how my artwork might be a perfect fit for your needs.

Warm regards,

Cecilia Kristoffersson
Art by CK

─────────────────────────────────────────────────────────────
This is an automated confirmation from Art by CK website.
For urgent matters, please contact me directly at {settings.CONTACT_EMAIL}

www.artbyck.com"""
        
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[contact_submission.email],
            fail_silently=False,
        )
        
        logger.info(f"Confirmation email sent successfully to {contact_submission.email}")
        return True
        
    except Exception as e:
        logger.error(f"Failed to send confirmation email to {contact_submission.email}: {str(e)}")
        return False