from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

# Create your forms here
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(max_length = 55, help_text='example@gmail.com')

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')