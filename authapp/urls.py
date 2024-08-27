from django.urls import path
from .views import login_view, logout_view, home_view

urlpatterns = [
    path('', login_view, name='login'),  # Default login view
    path('logout/', logout_view, name='logout'),  # Restrict logout to POST requests in the view
    path('dashboard/', home_view, name='home'),  # Use a non-obvious URL instead of 'home'
]
