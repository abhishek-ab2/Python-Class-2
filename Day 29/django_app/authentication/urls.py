from django.urls import path
from .views import register, login_request, dashboard, logout_request

urlpatterns = [
    path('register/', register),
    path('login/', login_request),
    path('logout/', logout_request),
    path('dashboard/', dashboard),
]