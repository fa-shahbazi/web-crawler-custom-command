from django.shortcuts import render
from .models import Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegistratinForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import generic
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'u loged in ','success')
                return redirect('crawler:category-list')
            else:
                messages.error(request, 'wrong username or password','warning')


    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form':form})

def user_register(request):
    if request.method == 'POST':
        form = UserRegistratinForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password1'])
            messages.success(request, 'u registered successfully', 'success')
            return redirect(reverse('accounts:user_login'))

    else:
        form = UserRegistratinForm()
    return render(request, 'accounts/register.html', {'form':form})


def user_logout(request):
    logout(request)
    messages.success(request,'logout successfully','success')
    return redirect('crawler:category-list')


# @login_required
# def user_profile(request, user_id):
#     user = get_object_or_404(User, pk=user_id)
#     if request.method == 'POST':
#         form = UserProfileForm(request.Post, instance=user.profile)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'your profile changed', 'success')
#             return redirect('crawler:category-list')
#     else:
#         form = UserProfileForm(instance=user.profile)
#     return render(request, 'accounts:profile.html', {'form':form})




