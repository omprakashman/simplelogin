from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
# from django.http import HttpResponse ## Remove this 
# from django.contrib import auth, messages ## Remove this 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import CustomPasswordChangeForm


def login_view(request):
    uname = None
    upass = None

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        uname = request.POST.get('username')
        upass = request.POST.get('password')
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to a home page or another URL
        else:
            print(f" OM:::>>> user password = {uname}, password = {upass}")
            return render(request, 'error.html', {
                'user': uname,
                'password': upass,
                'form': form
            })
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})



@login_required
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page or another URL

@login_required
def home_view(request):
    return render(request, 'success.html')


@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Keep the user logged in after changing password
            return redirect('home')  # Redirect to a home page or another URL
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})


def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def error_500_view(request):
    return render(request, '500.html', status=500)


