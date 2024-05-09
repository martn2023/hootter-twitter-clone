from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(
        max_length=300,  # Sets the maximum character length for validation
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'maxlength': 300,  # HTML attribute to prevent typing more than 300 characters
            'placeholder': 'Share your wisdom...'
        }),
        label='Content',
    )

    class Meta:
        model = Post
        fields = ['content']
