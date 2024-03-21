from django.urls import path
from .views import register, login_request, dashboard, logout_request, DashboardView

urlpatterns = [
    path('register/', register),
    path('login/', login_request),
    path('logout/', logout_request),
    path('dashboard/', dashboard),
    path('dashboard/<id>/', dashboard),
    path('dashboard-cl-based/', DashboardView.as_view()),
]