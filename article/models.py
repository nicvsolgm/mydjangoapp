from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class Article(models.Model):
    a_title = models.CharField(max_length=100)
    a_content = models.TextField()
    a_date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    a_image = models.ImageField(
        default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.a_title

    def get_absolute_url(self):
        return reverse("article-home")

    def save(self, *args, **kwargs):
       super().save(*args, **kwargs)
