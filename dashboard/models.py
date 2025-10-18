from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class GalleryImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AvailableArt(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='available_art/')
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class JournalEntry(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='journal/', blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class About(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "About Section"

class Exhibition(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='exhibition/', blank=True, null=True)
    video = CloudinaryField('video', resource_type='video', blank=True, null=True)
    description = models.TextField(blank=True)
    date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Exhibitions"
