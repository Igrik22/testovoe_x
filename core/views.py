import string
from random import choice

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from core.forms import CreateUserForm, LinkForm
from core.models import ShortLink, User


def home_page(request):
    return render(request, 'home.html')


def register_page(request):
    if request.user.is_authenticated:
        return redirect('shortener')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('shortener')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('shortener')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)


@login_required(login_url='login')
def url_short(request):
    current_user = request.user
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            key = ''.join(choice(string.ascii_letters) for _ in range(3))
            url = form.cleaned_data['url']
            new_url = ShortLink(long_link=url, key=key, short_link='http://127.0.0.1:8000/' + key, user=current_user)
            new_url.save()
            return redirect('/')
    else:
        form = LinkForm()
    context = {
        'form': form,
    }
    return render(request, 'shortener.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def list_shortener(request):
    short_urls = ShortLink.objects.filter(user=request.user.id).only('short_link', 'long_link')
    context = {'short_urls': short_urls}
    return render(request, 'list_shortener.html', context)


