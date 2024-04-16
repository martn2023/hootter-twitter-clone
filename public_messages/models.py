from django.db import models
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField(max_length=280)
    creation_time = models.DateTimeField(auto_now_add=True)
    parent_post = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name="replies")

    def __str__(self):
        return f"{self.author.username}: {self.content[:50]}..."

    @property
    def is_reply(self):
        return self.parent_post is not None
