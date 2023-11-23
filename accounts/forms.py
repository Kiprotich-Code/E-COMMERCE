from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# Create your forms here 
class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus':True}))

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.TextInput(max_length=50)
    last_name = forms.TextInput(max_length=50)

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
