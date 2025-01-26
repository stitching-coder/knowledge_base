from django.contrib import admin
from .models import HabitEntry

@admin.register(HabitEntry)
class HabitEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'trigger', 'notes', 'created_at', 'updated_at')
    search_fields = ('name', 'type', 'trigger', 'tags')
    list_filter = ('created_at', 'updated_at')
