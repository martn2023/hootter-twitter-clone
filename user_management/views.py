from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse

from django.contrib.auth.models import User

from .forms import ExtendedUserCreationForm
from django.db.models import Count, Q, F #take note that Q and F are terms of art used by Django
from public_messages.models import Post

def login_start(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next')  # Get the next URL from the form
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url:
                return redirect(next_url)  # Redirect to the next URL if provided
            else:
                return redirect('/')  # Redirect to the root URL
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('login_start')
    else:
        return render(request, 'user_management/login_start.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def register_new_user(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')  # Redirect to a home page or similar
    else:
        form = ExtendedUserCreationForm()
    return render(request, 'user_management/register_new_user.html', {'form': form})


def ExtendedUserProfileDetails(request, user_id):
    if not request.user.is_authenticated:
        return redirect('user_management:login_start')

    user = get_object_or_404(User, pk=user_id)
    try:
        profile = user.extended_profile
    except ExtendedUserProfile.DoesNotExist:
        return HttpResponse("The user's profile does not exist.", status=404)

    return render(request, 'user_management/user_profile_view.html', {'user_profile': profile})

@login_required
def profile_edit(request):
    # Since the user is logged in, request.user will be the User instance
    try:
        user_profile = request.user.extended_profile
    except ExtendedUserProfile.DoesNotExist:
        # Handle the case if for some reason the profile does not exist
        user_profile = ExtendedUserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        # Process the form data
        bio = request.POST.get('bio', '')
        user_profile.bio = bio
        user_profile.save()
        # Redirect to the profile view page after saving
        return redirect('user_management:user_details', user_id=request.user.id)

    # If it's a GET request, display the form with the current bio
    return render(request, 'user_management/user_profile_edit.html', {'user_profile': user_profile})


def list_users(request):
    users = User.objects.all().order_by('username')

    # Posters: Users who have at least one original post (a post with no parent)
    posters = User.objects.filter(posts__parent_post__isnull=True).distinct()

    # Repliers: Users who have at least one reply and no original posts
    repliers = User.objects.annotate(
        total_posts=Count('posts'),
        reply_posts=Count('posts', filter=Q(posts__parent_post__isnull=False))
    ).filter(total_posts=F('reply_posts'), total_posts__gt=0).distinct()

    # Readers: Users who have not authored any posts
    readers = User.objects.exclude(id__in=posters).exclude(id__in=repliers)

    context = {
        'posters': posters,
        'repliers': repliers,
        'readers': readers
    }
    return render(request, 'user_management/list_users.html', context)

def list_readers(request):
    # Users who have authored posts
    users_with_posts = User.objects.filter(posts__isnull=False).distinct()

    # Readers: Users who have not authored any posts
    readers = User.objects.exclude(id__in=users_with_posts).order_by('username')

    context = {
        'readers': readers
    }
    return render(request, 'user_management/list_readers.html', context)


def list_posters(request):
    # Users who have authored at least one original post (a post with no parent)
    posters = User.objects.filter(posts__parent_post__isnull=True).distinct()

    context = {
        'posters': posters
    }
    return render(request, 'user_management/list_posters.html', context)


def list_user_categories(request):
    # Fetch all users
    all_users = User.objects.all().order_by('username')

    # Fetch users who have made any posts
    users_with_posts = User.objects.filter(posts__isnull=False).distinct()

    # Fetch users who have made at least one original post (a post with no parent)
    posters = User.objects.filter(posts__parent_post__isnull=True).distinct()

    context = {
        'all_users': all_users,
        'users_with_posts': users_with_posts,
        'posters': posters
    }
    return render(request, 'user_management/user_categories.html', context)