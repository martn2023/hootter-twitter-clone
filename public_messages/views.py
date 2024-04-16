from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required
def create_post(request):
    if request.method == "POST":
        content = request.POST.get("content")
        parent_id = request.POST.get("parent_id", None)
        Post.objects.create(author=request.user, content=content, parent_post_id=parent_id)
        return redirect('public_messages:post_list')
    return render(request, 'public_messages/public_message_compose_form.html')
