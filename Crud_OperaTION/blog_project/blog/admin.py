from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')  # Display columns in admin panel
    search_fields = ('title', 'content')    # Add search functionality
    ordering = ('-created_at',)            # Order by creation date
