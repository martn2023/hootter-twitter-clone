from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models import Count

from .models import ExtendedUserProfile, FollowerRelationship

# Define a new User admin with extended functionality
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff', 'following_count', 'followers_count')

    def following_count(self, obj):
        # Ensure to use the correct related name from FollowerRelationship model
        return obj.following.count()
    following_count.short_description = 'Following'

    def followers_count(self, obj):
        # Ensure to use the correct related name from FollowerRelationship model
        return obj.followers.count()
    followers_count.short_description = 'Followers'

# Safely unregister the old UserAdmin if it's registered
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass
admin.site.register(User, UserAdmin)

class ExtendedUserProfileAdmin(admin.ModelAdmin):
    list_display = ('get_user_id', 'user', 'bio')

    def get_user_id(self, obj):
        return obj.user.id
    get_user_id.short_description = 'User ID'

admin.site.register(ExtendedUserProfile, ExtendedUserProfileAdmin)

class FollowerRelationshipAdmin(admin.ModelAdmin):
    list_display = ('follower', 'followed', 'id')
    search_fields = ('follower__username', 'followed__username')

admin.site.register(FollowerRelationship, FollowerRelationshipAdmin)
