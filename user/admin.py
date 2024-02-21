from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django import forms


class UserChangeForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = '__all__'


# Регистрация модели пользователя с кастомной формой
class CustomUserAdmin(BaseUserAdmin):
    form = UserChangeForm
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональные данные: ', {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
        ('Права пользователя: ', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Даты: ', {'fields': ('last_login', 'date_joined')}),
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Ползователи'


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

