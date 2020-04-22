from django.shortcuts import render, redirect
from blog_app.forms import UserForm, UserProfileInfoForm, NewpostForm

from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from blog_app.models import Newpost
from datetime import datetime


@login_required
def index(request):
    posts = Newpost.objects.all().order_by('-published_date')
    return render(request, 'blog_app/index.html', {'posts': posts})


@login_required
def new_post(request):
    if request.method == 'POST':
        postform = NewpostForm(request.POST)
        if postform.is_valid():
            post = postform.save(commit=False)
            post.author = request.user
            post.published_date = datetime.now()
            post.save()
            return HttpResponseRedirect(reverse('blog_app:index'))
    postform = NewpostForm()
    return render(request, 'blog_app/create_post.html', {'postform': postform})


def sign_up(request):

    signup_status = ''

    if request.method == 'POST':
        userform = UserForm(request.POST)
        profileform = UserProfileInfoForm(request.POST)

        if userform.is_valid() and profileform.is_valid():
            user = userform.save(commit=False)
            user.username = (user.first_name + ' ' + user.last_name).title()
            user.set_password(user.password)
            user.save()

            profile = profileform.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            signup_status = 'Thank you for signing up'

    userform = UserForm()
    profileform = UserProfileInfoForm()
    return render(request, 'blog_app/sign_up.html', {'userform': userform,
                                                     'profileform': profileform,
                                                     'signup_status': signup_status})


def user_login(request):
    login_status = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('blog_app:index'))

            else:
                login_status = 'This user is not active now!'
        else:
            login_status = 'USER NOT AUTHENTICATED!'

    return render(request, 'blog_app/login.html', {'login_status': login_status,
                                                   'signup_status': request.session.get('signup_status')})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog_app:user_login'))
