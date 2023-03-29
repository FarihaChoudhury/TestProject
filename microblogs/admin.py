"""Configuration of the administrative interface for microblogs. """
from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Configuration of the admininterface for users."""

    list_display = [
        'username', 'first_name',
    ]
