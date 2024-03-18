from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm


def register(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
    else:
        form = RegistrationForm()

    return render(request, 'signup.html', {
        'form': form
    })


def login_request(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                login(request, user)
                return redirect('/auth/dashboard')
            else:
                return redirect('/auth/register')
    else:
        form = LoginForm()

    return render(request, 'signup.html', {
        'form': form
    })


@login_required(login_url='/auth/login')
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard.html', {
            'user': request.user,
            'first_name': request.user.first_name
        })

@login_required
def logout_request(request):
    logout(request)
    request.session.clear()
    return redirect('/auth/login')
