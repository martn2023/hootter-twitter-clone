from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import transaction
from .models import ExtendedUserProfile  # Import the ExtendedUserProfile model

class ExtendedUserCreationForm(UserCreationForm):
    bio = forms.CharField(max_length=300, required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'bio')

    def save(self, commit=True):
        with transaction.atomic():
            user = super().save(commit=False)
            if commit:
                user.save()
                # Assuming the profile is automatically created by the signal on user save
                profile, created = ExtendedUserProfile.objects.get_or_create(user=user)
                profile.bio = self.cleaned_data['bio']
                profile.save()
            return user
