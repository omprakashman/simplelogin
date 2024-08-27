from django.urls import path
from .views import login_view, logout_view, home_view

urlpatterns = [

    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),  # Commented out to avoid using /home
]
