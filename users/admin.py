from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User

# Register your models here.

class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    list_display_links = ['email']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
    search_fields = ['first_name', 'last_name', 'email']


admin.site.register(User, UserAdmin)
