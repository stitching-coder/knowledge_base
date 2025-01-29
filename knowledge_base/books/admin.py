from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_id', 'date', 'dewey_decimal', 'dewey_wording', 'dimensions', 'entry_date', 'height', 'isbn', 'isbns', 'lc_classification', 'length', 'media', 'page_count', 'physical_description', 'primary_author', 'primary_author_role', 'publication', 'secondary_author', 'secondary_author_role', 'source', 'subjects', 'summary', 'tags', 'thickness', 'title', 'weight', 'work_id','created_at', 'updated_at')
    search_fields = ('title', 'isbn', 'primary_author', 'tags')
    list_filter = ('created_at', 'updated_at')
