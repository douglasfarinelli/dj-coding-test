# ! coding: utf-8

from django.contrib import admin
from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):

    list_filter = [
        'department',
        'created_at'
    ]

    list_display = [
        'email',
        'name',
        'department'
    ]
