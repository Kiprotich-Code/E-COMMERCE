from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import UserSignupForm, CustomAuthenticationForm


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = UserSignupForm
    form = CustomAuthenticationForm
    model = CustomUser
    list_display_links = ['email']
    search_fields = ['email',]
    ordering = ('email', )
    list_display = ('email', )