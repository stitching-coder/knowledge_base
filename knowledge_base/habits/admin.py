from django.contrib import admin
from .models import Habit

@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'trigger', 'notes', 'created_at', 'updated_at')
    search_fields = ('name', 'type', 'trigger', 'tags')
    list_filter = ('created_at', 'updated_at')
