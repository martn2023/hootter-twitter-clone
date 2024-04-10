from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class ExtendedUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extended_profile')
    bio = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

# Signal to create or update the user profile whenever a User instance is created or saved
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        ExtendedUserProfile.objects.create(user=instance)
    else:
        instance.extended_profile.save()
