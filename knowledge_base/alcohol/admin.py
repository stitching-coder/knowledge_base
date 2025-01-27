from django.contrib import admin
from .models import Beverage

@admin.register(Beverage)
class BeverageAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'distiller', 'notes', 'alcohol_content', 'price','created_at', 'updated_at')
    search_fields = ('name', 'type', 'distiller', 'tags')
    list_filter = ('created_at', 'updated_at')
