from django.contrib import admin
from .models import StitchingProjectEntry


@admin.register(StitchingProjectEntry)
class StitchingProjectEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'status', 'stitching_type', 'type', 'tags', 'created_at', 'updated_at')
    search_fields = ('name', 'creator', 'status', 'tags')
    list_filter = ('created_at', 'updated_at')
