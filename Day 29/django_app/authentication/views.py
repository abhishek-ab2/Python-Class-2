from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q, F, Count
from django.db.models.aggregates import Sum, Max
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.views import View

from .forms import RegistrationForm, LoginForm, UserUpdateForm
from .models import Blog


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


def blog_list(request):
    blogs = Blog.objects.all()

    ordered_by_id_and_title_desc = blogs.order_by('-title', 'id')

    # blogs views is gt 30 or likes is less than 30
    # blogs = blogs.filter(Q(views__gt=30) | Q(likes__lt=30)) # For OR operation on conditions

    # blogs views is gt 50 and (likes is gt 30  or likes is lt 10)
    # blogs = blogs.filter(Q(views__gt=50) & (Q(likes__gt=30) | Q(likes__lt=10)))

    # blogs views is not gt 50
    # blogs = blogs.filter(~Q(views__gt=50))

    # blogs views is not gt 50 and (likes is gt 30)
    # blogs = blogs.filter(~Q(views__gt=50) & Q(likes__gt=30))

    # a new column "interaction" which is sum of likes and views
    # SQL: select *, add(likes, views) as interaction from blogs;
    blogs = blogs.annotate(interaction=F('likes') + F('views'))

    return render(request, 'blog-list.html', {
        'blogs': blogs
    })
