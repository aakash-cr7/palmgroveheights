from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST

@require_GET
@login_required
def home(request):
    template = 'home.html'
    data = {}
    return render(request, template, data)

@require_GET
def logout(request):
    auth_logout(request)
    return redirect('/')

@require_http_methods(['GET', 'POST'])
def index(request):
    template = 'index.html'
    data = {}

    if request.user.is_authenticated():
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        data['errors'] = []
        data['email'] = email
        if not email or not password:
            data['errors'].append('Please make sure you entered the username and password')
        else:
            user = authenticate(username = email, password = password)
            print user
            if user is None:
                data['errors'].append('Invalid email or password')
            elif not user.is_active:
                data['errors'].append('User not activated by admin')
            else:
                auth_login(request, user)
                return redirect('home')
    return render(request, template, data)

def signup(request):
    template = 'signup.html'
    data = {}
    return render(request, template, data)