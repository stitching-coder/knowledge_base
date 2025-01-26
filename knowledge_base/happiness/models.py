from django.db import models
from django.utils import timezone


class WordOfTheYear(models.Model):
    year = models.IntegerField()
    word = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name_plural = "Words"


class Entry(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Entries"
