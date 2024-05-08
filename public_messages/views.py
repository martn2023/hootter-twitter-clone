from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm  # Ensure this is imported here
from django.contrib import messages
from django.shortcuts import render, redirect

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect('public_messages:create_post')
    else:
        form = PostForm()

    return render(request, 'public_messages/public_message_compose_form.html', {'form': form})


def own_posts(request):
    if not request.user.is_authenticated:
        return redirect('user_management:login')
    else:
        user_posts = Post.objects.filter(author=request.user).order_by('-creation_time')
        return render(request, 'public_messages/my_posts.html', {'posts': user_posts})

    # A safety net, although ideally every condition should be handled explicitly
    return redirect('some_default_page')