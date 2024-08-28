from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash
from .forms import CustomPasswordChangeForm
from django.contrib import messages
from .forms import CustomUserCreationForm  # Import your custom form
from .models import UserProfile  # Import UserProfile


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
            messages.success(request, 'Logged in  successfully')  # Add success message
            return redirect('home')  # Redirect to a home page or another URL
        else:
            messages.error(request, f'The username {uname} and Password *** are incorrect')  # Add success message
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
    messages.success(request, 'You have been logged out of the system')  # Add success message
    return redirect('login')  # Redirect to the login page or another URL

@login_required
def home_view(request):
     return render(request, 'success.html')


@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, request.user)  # Keep the user logged in after changing password
            messages.success(request, 'Password changed successfully')  # Add success message
            return redirect('home')  # Redirect to a home page or another URL
        else :
            messages.error(request, 'Incorrect current password')  # Add success message
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})

# User Registration
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        uname = request.POST.get('username')
        
        if form.is_valid():
            user = form.save()
            '''
            profile = UserProfile.objects.create(
                user=user,
                full_name=form.cleaned_data['full_name'],
                email=form.cleaned_data['email'],
                mobile_number=form.cleaned_data['mobile_number'],
                address=form.cleaned_data['address']
            )
            '''
            messages.success(request, f'User id [ {uname} ] created successfully !!. Pl. log in, to activate your user id with details')
            return redirect('login')
        else:
            messages.error(request, 'There was an error with your registration. Please try again.')
            # return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def error_500_view(request):
    return render(request, '500.html', status=500)


