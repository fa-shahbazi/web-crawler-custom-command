from django.shortcuts import render
from .models import Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegistratinForm, ActivationCodeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import generic
from django.core.cache import cache
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
import random


def generate_code():
    return random.randint(10000, 99999)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'u logged in ', 'success')
                return redirect('store:category-list')
            else:
                messages.error(request, 'wrong username or password', 'warning')


    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegistratinForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            code = generate_code()
            cache.set('username', cd['username'], timeout=60)
            cache.set('email', cd['email'], timeout=60)
            cache.set('password', cd['password1'], timeout=60)
            cache.set('code', code, timeout=60)
            if code is None:
                messages.error(request, 'Too Late', 'warning')
            print(code)
            activation_form = ActivationCodeForm()
            return render(request, 'accounts/confirm_code.html', {'form': activation_form})
    else:
        form = UserRegistratinForm()
    return render(request, 'accounts/register.html', {'form': form})


def confirm_registration(request):
    form = ActivationCodeForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            code = form.cleaned_data['code']
            cache_code = cache.get('code')
            if not cache_code == code:
                return redirect('accounts:user_login')
            username = cache.get('username')
            password = cache.get('password')
            email = cache.get('email')
            user = User.objects.create_user(username=username, password=password, email=email)
            login(request,user)
            return redirect('/')
    return redirect('accounts:user_login')


def user_logout(request):
    logout(request)
    messages.success(request, 'logout successfully', 'success')
    return redirect('store:category-list')

# @login_required
# def user_profile(request, user_id):
#     user = get_object_or_404(User, pk=user_id)
#     if request.method == 'POST':
#         form = UserProfileForm(request.Post, instance=user.profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'your profile changed', 'success')
#             return redirect('store:category-list')
#     else:
#         form = UserProfileForm(instance=user.profile)
#     return render(request, 'accounts:profile.html', {'form':form})
