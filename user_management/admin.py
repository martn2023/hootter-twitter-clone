from django.contrib import admin
from .models import ExtendedUserProfile

class ExtendedUserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio',)  # Customize the fields displayed in the admin panel

# Register the ExtendedUserProfileAdmin class with the admin site
admin.site.register(ExtendedUserProfile, ExtendedUserProfileAdmin)
