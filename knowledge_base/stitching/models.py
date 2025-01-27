from django.db import models
from django.utils import timezone


class StitchingProjectEntry(models.Model):
    name = models.CharField(max_length=200)
    creator = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    stitching_type = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    tags = models.CharField(max_length=200, blank=True)
    image_filename = models.CharField(max_length=200, default='image.jpg')
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Stitching Projects"
