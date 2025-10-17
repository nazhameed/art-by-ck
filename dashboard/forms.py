from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Field, Layout, Row
from crispy_bootstrap5.bootstrap5 import Switch

from .models import GalleryImage, AvailableArt, JournalEntry, About, Exhibition
from cloudinary.uploader import upload as cloudinary_upload


class DashboardCrispyMixin:
    """Shared crispy-forms helper configuration for admin dashboard forms."""

    helper_layout: tuple = ()

    def _init_helper(self):
        self.helper = FormHelper()
        self.helper.form_tag = False
        layout_elements = []
        for item in self.helper_layout:
            layout_elements.append(Field(item) if isinstance(item, str) else item)
        self.helper.layout = Layout(*layout_elements)


class GalleryImageForm(DashboardCrispyMixin, forms.ModelForm):
    helper_layout = ("title", "image", "description")

    class Meta:
        model = GalleryImage
        fields = ["title", "image", "description"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_helper()


class AvailableArtForm(DashboardCrispyMixin, forms.ModelForm):
    helper_layout = ("title", "image", "price", "description", Switch("is_available"))

    class Meta:
        model = AvailableArt
        fields = ["title", "image", "price", "description", "is_available"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_helper()


class JournalEntryForm(DashboardCrispyMixin, forms.ModelForm):
    helper_layout = ("title", "image", "content")

    class Meta:
        model = JournalEntry
        fields = ["title", "image", "content"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_helper()


class AboutForm(DashboardCrispyMixin, forms.ModelForm):
    helper_layout = ("text", "image")

    class Meta:
        model = About
        fields = ["text", "image"]
        widgets = {
            "text": forms.Textarea(attrs={"rows": 6, "class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_helper()


class ExhibitionForm(DashboardCrispyMixin, forms.ModelForm):
    helper_layout = (
        "title",
        "image",
        "video",
        "description",
        Row(
            Column(Field("date"), css_class="col-md-6"),
            Column(Field("location"), css_class="col-md-6"),
        ),
    )

    class Meta:
        model = Exhibition
        fields = ["title", "image", "video", "description", "date", "location"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
            "date": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "video": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_helper()

    def save(self, commit=True):
        instance = super().save(commit=False)
        video_file = self.cleaned_data.get("video")
        if video_file:
            result = cloudinary_upload(video_file, resource_type="video")
            instance.video = result["public_id"]
        if commit:
            instance.save()
        return instance
