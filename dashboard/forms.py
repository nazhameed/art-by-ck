from django import forms
from .models import GalleryImage, AvailableArt, JournalEntry

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['title', 'image', 'description']

class AvailableArtForm(forms.ModelForm):
    class Meta:
        model = AvailableArt
        fields = ['title', 'image', 'price', 'description', 'is_available']

class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = JournalEntry
        fields = ['title', 'image', 'content']
