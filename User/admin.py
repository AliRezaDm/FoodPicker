from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

@admin.register(User)
class CustomAdminUser(UserAdmin):

    model = User

    list_display = ['email', 'name', 'phone_number', 'is_active', 'is_staff', 'created_at', 'thumbnail_tag']
    list_filter = ('is_active', 'is_staff', 'created_at')
    search_fields = ('email', 'name', 'phone_number')
    ordering = ('-created_at', )

    fieldsets = (
        ('Personal_Info', {'fields' : ('avatar', 'name', 'email', 'phone_number')}),
        ('Permissions', {'fields' : ('is_active', 'is_staff', 'is_superuser')}),
        ('Important_Date', {'fields' : ('last_login', 'created_at')}),
        )    
    
    add_fieldsets = (
        ('Create User', {
            'classes' : ('wide', ), 
            'fields'  : ('email', 'name', 'phone_number', 'password1', 'password2', 'is_active', 'is_staff')
        })
    )

    readonly_fields = ('created_at', 'last_login', 'thumbnail_tag')

    