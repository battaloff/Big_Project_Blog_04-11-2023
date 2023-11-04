from django.contrib import admin
from .models import Posts


@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

