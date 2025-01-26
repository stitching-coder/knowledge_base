from django.contrib import admin
from .models import WordOfTheYear, Entry


@admin.register(WordOfTheYear)
class WordOfTheYearAdmin(admin.ModelAdmin):
    list_display = ('word', 'year', 'created_at', 'updated_at')
    search_fields = ('word', 'year')
    list_filter = ('year', 'created_at', 'updated_at')


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'tags')
    list_filter = ('created_at', 'updated_at')
