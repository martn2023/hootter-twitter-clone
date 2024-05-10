from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

class ExtendedUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extended_profile')
    bio = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

# Signal to create or update the user profile whenever a User instance is created
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        ExtendedUserProfile.objects.get_or_create(user=instance)
    # No need for an else clause if you're not updating the profile here

class FollowerRelationship(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following")
    followed = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followers")

    class Meta:
        unique_together = ('follower', 'followed')  # Ensure a user cannot follow the same person more than once

    def __str__(self):
        return f"{self.follower.username} follows {self.followed.username}"