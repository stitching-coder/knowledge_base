from django.db import models
from django.utils import timezone


class Book(models.Model):
    book_id = models.IntegerField()
    date = models.IntegerField()
    dewey_decimal = models.CharField(max_length=50, blank=True)
    dewey_wording = models.TextField(blank=True)
    dimensions = models.CharField(max_length=50, blank=True)
    entry_date = models.CharField(max_length=10, blank=True)
    height = models.CharField(max_length=50, blank=True)
    isbn = models.CharField(max_length=50, blank=True)
    isbns = models.CharField(max_length=50, blank=True)
    lc_classification = models.CharField(max_length=50, blank=True)
    length = models.CharField(max_length=50, blank=True)
    media = models.CharField(max_length=50, blank=True)
    page_count = models.CharField(max_length=50, blank=True)
    physical_description = models.CharField(max_length=50, blank=True)
    primary_author = models.CharField(max_length=200, blank=True)
    primary_author_role = models.CharField(max_length=50, blank=True)
    publication = models.CharField(max_length=500, blank=True)
    secondary_author = models.CharField(max_length=200, blank=True)
    secondary_author_role = models.CharField(max_length=50, blank=True)
    source = models.CharField(max_length=50, blank=True)
    subjects = models.CharField(max_length=50, blank=True)
    summary = models.TextField(blank=True)
    tags = models.CharField(max_length=200, blank=True)
    thickness = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=200, blank=True)
    weight = models.CharField(max_length=50, blank=True)
    work_id = models.CharField(max_length=50, blank=True)
    image_filename = models.CharField(max_length=200, default='image.jpg')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Books"
