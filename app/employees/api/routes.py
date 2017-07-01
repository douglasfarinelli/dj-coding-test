# ! coding: utf-8

from app.urls_api import V1_ROUTES
from .views import EmployeeViewSet

V1_ROUTES.register('employees', EmployeeViewSet)
