# ! coding: utf-8

from rest_framework import mixins, viewsets
from ..models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    """Employee API Endpoint"""

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
