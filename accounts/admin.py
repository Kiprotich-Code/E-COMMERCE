from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import UserSignupForm, CustomAuthenticationForm, CustomUserChangeForm


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserChangeForm
    model = CustomUser
    list_display_links = ['email']
    search_fields = ['email',]
    ordering = ('-date_joined', )
    list_display = ('email', 'is_staff', 'is_active', 'date_joined', )
    list_filter = ('email', 'is_staff', 'is_active', 'date_joined',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', )}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups',)}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),   
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active',)
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)