from django.shortcuts import render
from .forms import RegistrationForm


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


