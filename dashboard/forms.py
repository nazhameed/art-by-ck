from django import forms
from .models import GalleryImage, AvailableArt, JournalEntry, About, Exhibition
from cloudinary.uploader import upload as cloudinary_upload

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

class AboutForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['text', 'image']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 6, 'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ExhibitionForm(forms.ModelForm):
    class Meta:
        model = Exhibition
        fields = ['title', 'image', 'video', 'description', 'date', 'location']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True):
        instance = super().save(commit=False)
        video_file = self.cleaned_data.get('video')
        if video_file:
            result = cloudinary_upload(video_file, resource_type='video')
            instance.video = result['public_id']
        if commit:
            instance.save()
        return instance
