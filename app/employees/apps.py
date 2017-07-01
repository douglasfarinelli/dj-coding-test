# ! coding: utf-8

from core import apps
from django.apps import AppConfig


class EmployeesConfig(apps.ApiAppConfigMixin, AppConfig):
    name = 'employees'
