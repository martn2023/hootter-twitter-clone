# user_management/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ExtendedUserProfile

class ExtendedUserCreationForm(UserCreationForm):
    bio = forms.CharField(max_length=300, required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'bio')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            ExtendedUserProfile.objects.create(user=user, bio=self.cleaned_data['bio'])
        return user
