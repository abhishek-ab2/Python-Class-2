from django.urls import path
from .views import home, create_order

urlpatterns = [
    path('home/', home),
    path('create/', create_order)
]
