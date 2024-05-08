from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ExtendedUserCreationForm(UserCreationForm):
    bio = forms.CharField(max_length=300, required=False)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'bio')

    def save(self, commit=True):
        user = super().save(commit=commit)  # Just save the User object
        return user
