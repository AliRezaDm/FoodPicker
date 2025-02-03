from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

@admin.register(User)
class CustomAdminUser(UserAdmin):

    model = User

    list_display = ['email', 'name', 'phone_number', 'is_active', 'is_staff', 'created_at', 'avatar_tag']
    list_filter = ('is_active', 'is_staff', 'created_at')
    search_fields = ('email', 'name', 'phone_number')
    ordering = ('-created_at', )

    fieldsets = (
        ('Personal_Info', {'fields' : ('avatar', 'name', 'email', 'phone_number')}),
        ('Permissions', {'fields' : ('is_active', 'is_staff', 'is_superuser')}),
        ('Important_Date', {'fields' : ('last_login', 'created_at')}),
        )    
    
    add_fieldsets = (
    (None, {
        'classes': ('wide',),
        'fields': ('email', 'name', 'phone_number', 'password1', 'password2'),
    }),
)


    readonly_fields = ('created_at', 'last_login', 'avatar_tag')

    def avatar_tag(self, obj):
        """Display user avatar in admin panel"""
        if obj.avatar:
            return f'<img src="{obj.avatar.url}" width="50" height="50" style="border-radius: 10px;">'
        return "No Image"
    
    avatar_tag.allow_tags = True
    avatar_tag.short_description = 'Avatar'