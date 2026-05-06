from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'user_name', 'first_name', 'last_name', 'is_publisher', 'created_at')
    search_fields = ('email', 'user_name', 'first_name', 'last_name')
    list_filter = ('is_publisher', 'created_at')    