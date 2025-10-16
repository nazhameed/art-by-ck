from django.db import models

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

class ImmersiveHero(models.Model):
    image = models.ImageField(upload_to='immersive/hero/')
    caption = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Immersive Hero (updated {self.updated_at:%Y-%m-%d})"

class ImmersiveMedia(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]
    hero = models.ForeignKey(ImmersiveHero, on_delete=models.CASCADE, related_name='media', null=True, blank=True)
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES, default='image')
    image = models.ImageField(upload_to='immersive/media/', blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
