from django.contrib import admin
from django.utils.html import format_html

from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'year', 'display_image')
    list_filter = ('title', 'description', 'author', 'year')

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />'.format(obj.image.url))
        else:
            return 'No Image'
    
    display_image.short_description = 'Image'