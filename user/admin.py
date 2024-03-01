from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django import forms
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class UserChangeForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = '__all__'


class UserResource(resources.ModelResource):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_active', 'user_permissions')
        skip_unchanged = True


class CustomUserAdmin(ImportExportModelAdmin, BaseUserAdmin):
    list_display = BaseUserAdmin.list_display + ('id',)
    form = UserChangeForm
    resource_class = UserResource
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональная информация: ', {'fields': ('first_name', 'last_name', 'email', 'phone_number')}),
        ('Права пользователя: ', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'



admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

