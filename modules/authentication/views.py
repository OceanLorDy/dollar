from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'auth/login.html', {'auth_is_active_error': True})
        else:
            return render(request, 'auth/login.html', {'auth_login_error': True})
    else:
        return render(request, 'auth/login.html', {})


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')
