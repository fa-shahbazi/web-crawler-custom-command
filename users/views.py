from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserLoginForm, UserRegistratinForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user  =authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # messages.success(request, 'u loged in ','success')
                return redirect('crawler:category-list')
            # else:
                # messages.error(request, 'wrong username','warning')


    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form':form})

def user_register(request):
    if request.method == 'POST':
        form =UserRegistratinForm(request.POST)
        if form.is_valid():
            cd =form.cleaned_data
            User.objects.create_user(cd['username'], cd['email'], cd['password1'])
            # messages.success(request, 'u registered successfully', 'success')
            return redirect('users:user_login')

    else:
        form = UserRegistratinForm()
    return render(request, 'users/register.html', {'form':form})


def user_logout(request):
    logout(request)
    # messages.success(request,'logout successfully','success')
    return redirect('crawler:category-list')