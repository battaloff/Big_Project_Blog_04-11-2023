from django.db import models
from django.utils import timezone


class Posts(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = models.TextField

    publish = models.DateTimeField(default=timezone.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title