from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required

@login_required
def create_post(request, parent_id=None):
    parent_post = None
    if parent_id:
        parent_post = get_object_or_404(Post, id=parent_id)  # Ensure parent post exists

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.parent_post = parent_post  # Set this post as a reply if parent_id exists
            post.save()
            messages.success(request, "Your message has been posted!")
            return redirect('public_messages:post_list')
    else:
        form = PostForm()

    return render(request, 'public_messages/public_message_compose.html', {
        'form': form,
        'parent_post': parent_post
    })