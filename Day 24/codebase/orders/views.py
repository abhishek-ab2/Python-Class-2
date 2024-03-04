from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'orders-home.html', {
        'orders': ['o1', 'o2', 'o3', 'o4']
    })
