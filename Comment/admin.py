from django.contrib import admin
from .models import Comment



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ['user', 'recipe', 'title', 'is_reply', 'created_at', 'status']
    search_fields = ('user__name','user__email', 'recipe__name', 'title')
    list_filter = ('status', 'is_reply', 'created_at')
    readonly_fields = ('created_at',)

