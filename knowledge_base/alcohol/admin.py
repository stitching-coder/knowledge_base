from django.contrib import admin
from .models import AlcoholEntry

@admin.register(AlcoholEntry)
class AlcoholEntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'distiller', 'notes', 'alcohol_content', 'price','created_at', 'updated_at')
    search_fields = ('name', 'type', 'distiller')
    list_filter = ('created_at', 'updated_at')
