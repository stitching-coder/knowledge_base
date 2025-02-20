from django.db import models
from django.utils import timezone


class Beverage(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    distiller = models.CharField(max_length=200)
    notes = models.TextField()
    alcohol_content = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=200, blank=True)
    image_filename = models.CharField(max_length=200, default='image.jpg')
    distiller_website = models.URLField(max_length=200, default='https://www.example.com')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Beverages"
