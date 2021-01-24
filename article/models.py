from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
# from PIL import Image


class Article(models.Model):
    a_title = models.CharField(max_length=100)
    a_content = RichTextField(blank=True, null=True)
    a_date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.a_title

    def get_absolute_url(self):
        return reverse("article-home")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Contact(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    message = models.TextField(default=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


