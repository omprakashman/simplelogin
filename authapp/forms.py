from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator  # Add this import

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Current Password'}),
        label='Current Password'
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'}),
        label='New Password'
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm New Password'}),
        label='Confirm New Password'
    )

#User Registration

'''
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=8, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User ID'}))
'''
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=8,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'User ID'}),
        validators=[
            RegexValidator(
                regex='^[a-zA-Z]*$',
                message='Username must contain only alphabets',
                code='invalid_username'
            )
        ]
    )
    
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
