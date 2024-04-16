from django.contrib import admin

from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import ExtendedUserProfile

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff')
    # You can keep the rest of the settings from BaseUserAdmin or customize as needed.

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class ExtendedUserProfileAdmin(admin.ModelAdmin):
    list_display = ('get_user_id', 'user', 'bio')

    def get_user_id(self, obj):
        return obj.user.id

    get_user_id.short_description = 'User ID'


admin.site.register(ExtendedUserProfile, ExtendedUserProfileAdmin)