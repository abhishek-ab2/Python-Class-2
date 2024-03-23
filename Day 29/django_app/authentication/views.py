from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.views import View

from .forms import RegistrationForm, LoginForm, UserUpdateForm


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
def dashboard(request, id=None):
    print(id)
    if request.user.is_authenticated:
        return render(request, 'dashboard.html', {
            'user': request.user,
            'first_name': request.user.first_name
        })


class DashboardView(View):
    def get(self, request):
        return HttpResponse(status=200, content='Good job')

    def post(self, request):
        pass


@login_required
def logout_request(request):
    logout(request)
    request.session.clear()
    return redirect('/auth/login')


def update_user(request):
    form = UserUpdateForm(instance=request.user, initial={
        'email': request.user.email
    })
    if request.POST:
        form = UserUpdateForm(data=request.POST, initial={'email': request.user.email}, instance=request.user)
        if form.is_valid():
            form.save()
    request.session['id'] = 23452345

    return render(request, 'user.html', {'form': form})

