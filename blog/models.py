from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=False, blank=True)
    unique_id = models.CharField(max_length=12, unique=True, blank=True, editable=False)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='static/thumbnails/', blank=True, null=True)  # <-- gambar kecil buat list
    featured_image = models.ImageField(upload_to='static/featured/', blank=True, null=True)  # <-- gambar utama buat detail
    featured_image2 = models.ImageField(upload_to='static/featured/', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    # save method tetep sama seperti sebelumnya ya~
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        if not self.unique_id:
            while True:
                candidate = get_random_string(length=10, allowed_chars='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
                if not Post.objects.filter(unique_id=candidate).exists():
                    self.unique_id = candidate
                    break

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/read/{self.created_date.strftime('%Y/%m/%d')}/{self.unique_id}/{self.slug}/"