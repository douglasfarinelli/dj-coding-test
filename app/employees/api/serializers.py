# ! coding: utf-8

from rest_framework import serializers, validators
from ..models import Employee


class EmployeeSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(validators=[
        validators.UniqueValidator(queryset=Employee.objects.all_actives_and_inatives())
    ])

    class Meta:
        fields = serializers.ALL_FIELDS
        model = Employee
