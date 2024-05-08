from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm  # Ensure this is imported here
from django.contrib import messages
from django.shortcuts import render, redirect

@login_required
def create_post(request, parent_id=None):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if parent_id:
                # Fetch the parent post using the given parent_id
                post.parent_post = get_object_or_404(Post, id=parent_id)
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect('public_messages:create_post')
    else:
        # If there's a parent_id, fetch the parent post and pass it to the form
        parent_post = get_object_or_404(Post, id=parent_id) if parent_id else None
        form = PostForm()

    return render(request, 'public_messages/public_message_compose_form.html', {
        'form': form,
        'parent_post': parent_post  # Make sure this is correctly passed
    })



def own_posts(request):
    if not request.user.is_authenticated:
        return redirect('user_management:login')
    else:
        user_posts = Post.objects.filter(author=request.user).order_by('-creation_time')
        return render(request, 'public_messages/my_posts.html', {'posts': user_posts})

    # A safety net, although ideally every condition should be handled explicitly
    return redirect('some_default_page')


def everyone_elses_posts(request):
    if not request.user.is_authenticated:
        return redirect('user_management:login')

    # Fetch posts where the author is not the current user
    posts = Post.objects.exclude(author=request.user).order_by('-creation_time')
    return render(request, 'public_messages/everyone_elses_posts.html', {'posts': posts})


def create_reply(author, content, parent_post_id):
    parent_post = Post.objects.get(id=parent_post_id)  # Get the parent post
    reply_post = Post(author=author, content=content, parent_post=parent_post)
    reply_post.save()
    return reply_post
