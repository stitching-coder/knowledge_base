from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'status', 'stitching_type', 'type', 'tags', 'created_at', 'updated_at')
    search_fields = ('name', 'creator', 'status', 'tags')
    list_filter = ('created_at', 'updated_at')
