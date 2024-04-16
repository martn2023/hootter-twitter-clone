from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_author_id', 'get_author_name', 'content', 'creation_time')
    search_fields = ['content', 'author__username']
    list_filter = ('creation_time', 'author')

    def get_author_id(self, obj):
        return obj.author.id

    get_author_id.short_description = 'Author ID'

    def get_author_name(self, obj):
        return obj.author.username

    get_author_name.short_description = 'Author Name'


admin.site.register(Post, PostAdmin)
