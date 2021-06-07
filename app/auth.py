from django.contrib.auth import authenticate, login, logout
from .forms import SignUpFormUser, UpdateUserForm, UpdateUserAvatar
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User


def user_register(request):
    current_user = request.user
    if current_user.is_authenticated:
        return redirect('app:dashboard')

    user_form = SignUpFormUser()
    if request.method == 'POST':
        user_form = SignUpFormUser(request.POST)
        if user_form.is_valid():
            user_form.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {username}')
            return redirect('app:signin')
    content = {
        'user_form': user_form,
        'title': 'Scientics - Sign up'
    }
    return render(request, 'auth/signup.html', content)


def user_login(request):
    current_user = request.user
    if current_user.is_authenticated:
        return redirect('app:dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            username = User.objects.get(email=username).username
        except User.DoesNotExist:
            pass
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('app:dashboard')
        else:
            messages.error(
                request, 'Username or password is invalid. Please try again.')
    content = {
        'title': "Scientics - Sign in"
    }
    return render(request, 'auth/signin.html', content)


@login_required(login_url='app:signin')
def user_profile(request, username):
    name = request.user.username
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        user_avatar_form = UpdateUserAvatar(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and user_avatar_form.is_valid():
            user_form.save()
            user_avatar_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Your profile was updated!')
            return redirect('app:profile', username=username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        user_avatar_form = UpdateUserAvatar(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'user_avatar_form': user_avatar_form,
        'title': f'Scientics - {name.capitalize()}'
    }
    return render(request, 'auth/profile.html', context)


@login_required(login_url='app:signin')
def user_logout(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect('app:signin')
