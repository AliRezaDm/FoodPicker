from django.contrib import admin
from .models import *



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug']
    search_fields = ['name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ['title', 'category_name', 'thumbnail_tag', 'created', 'updated']
    readonly_fields = ('thumbnail_tag',)
    search_fields = ['title', 'category_name']


    #to display category name
    def category_name(self, obj):
        return obj.category.name
    category_name.short_description = 'Category'