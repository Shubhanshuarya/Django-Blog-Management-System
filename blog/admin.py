from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Category
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'header_image', 'body', 'publish', 'created', 'updated', 'status']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'author', 'publish')
    search_fields = ('title', 'body')
    date_hierarchy = 'publish'
    raw_id_fields = ('author', 'category')
    ordering = ('status', 'publish')
    summernote_fields = ('body',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
