from django.contrib import admin
from django.utils.html import format_html
from .models import ContactSubmission


@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = [
        'name', 
        'email', 
        'inquiry_type', 
        'subject_truncated',
        'submitted_at', 
        'status_display',
    ]
    
    list_filter = [
        'inquiry_type',
        'is_read',
        'is_responded',
        'submitted_at',
    ]
    
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['submitted_at']
    ordering = ['-submitted_at']
    list_per_page = 10

    # Custom fieldsets for detail view
    fieldsets = [
            ('Contact Information', {
                'fields': ['name', 'email', 'phone', 'preferred_contact_method']
            }),
            ('Inquiry Details', {
                'fields': ['inquiry_type', 'subject', 'message']
            }),
            ('Artwork Information', {
                'fields': ['artwork_title', 'artwork_reference']
            }),
            ('Admin Tracking', {
                'fields': ['submitted_at', 'is_read', 'is_responded', 'response_notes']
            })
        ]
    
    # Custom actions
    actions = ['mark_as_read', 'mark_as_responded']

    def subject_truncated(self, obj):
        """Display truncated subject for clearer list view"""
        if len(obj.subject) > 25:
            # [:25] takes first 25 characters of string (index 0 to 24)
            return f"{obj.subject[:25]}..."
        return obj.subject
    subject_truncated.short_description = "Subject"
    
    def status_display(self, obj):
        """Display status with simple visual indicators"""
        if obj.is_responded:
            return format_html('<span style="color: green;">✓ Responded</span>')
        elif obj.is_read:
            return format_html('<span style="color: orange;">● Read</span>')
        else:
            return format_html('<span style="color: red;">● New</span>')
    status_display.short_description = "Status"
    
    # key features for message management, allows admin to update DB to reflect read/responded to status
    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f"{updated} submission(s) marked as read.")
    mark_as_read.short_description = "Mark as read"
    
    def mark_as_responded(self, request, queryset):
        updated = queryset.update(is_read=True, is_responded=True)
        self.message_user(request, f"{updated} submission(s) marked as responded.")
    mark_as_responded.short_description = "Mark as responded"
