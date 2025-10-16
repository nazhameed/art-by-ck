from django import forms
from .models import GalleryImage, AvailableArt, JournalEntry, ImmersiveHero, ImmersiveMedia

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

class ImmersiveHeroForm(forms.ModelForm):
    class Meta:
        model = ImmersiveHero
        fields = ['image', 'caption']

class ImmersiveMediaForm(forms.ModelForm):
    class Meta:
        model = ImmersiveMedia
        fields = ['media_type', 'image', 'video_url', 'title', 'description', 'order']
