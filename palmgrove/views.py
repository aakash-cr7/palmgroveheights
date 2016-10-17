from django.shortcuts import render, redirect, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_GET, require_POST

@require_http_methods(['GET', 'POST'])
@login_required
def discussions(request):
    template = 'discussions.html'
    data = {}
    return render(request, template, data)

@require_http_methods(['GET', 'POST'])
@login_required
def notices(request):
    template = 'notices.html'
    data = {}
    return render(request, template, data)