from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UserChangeForm
from .models import MyUser

class SignupForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ('email', 'date_of_birth', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    class Meta:
        model = MyUser
        fields = ('email', 'password')
class UserChangeForm(UserChangeForm):
    class Meta:
        model=MyUser
        fields=('email','date_of_birth','is_active','is_admin')