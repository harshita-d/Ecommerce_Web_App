from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.FileField(
        upload_to="category", blank=True, null=True, default="category.jpg"
    )
    active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Category"
        ordering = ["-title"]

    def __str__(self):
        return self.title
