from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import TestModel


@admin.register(TestModel)
class TestModelAdmin(ImportExportModelAdmin):
    list_display = ['title', 'number', 'user']
    search_fields = ['title', 'number', 'user__username']
    list_filter = ['user']
    ordering = ['title']
