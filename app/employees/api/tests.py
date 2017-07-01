# ! coding: utf-8

import json

from core.tests import SQLiteInMemoryMixin
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class EmployeeAPITest(SQLiteInMemoryMixin, APITestCase):
    """Simple test case for Employee API."""

    fixtures = [
        'employees/fixtures/employees.json'
    ]

    def setUp(self):
        self.content_type = 'application/json'
        self.new_employee = json.dumps({
            'email': 'douglas_farinelli@yahoo.com.br',
            'name': 'Douglas',
            'department': 'Technology'
        })
        self.employee_already_registered = json.dumps({
            "email": "joao@gmail.com",
            "name": "João",
            "department": "Technology"
        })

    def test_can_create_employee(self):
        response = self.client.post(
            reverse('v1:employee-list'),
            self.new_employee,
            content_type=self.content_type
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_can_create_non_unique_employee_email(self):
        response = self.client.post(
            reverse('v1:employee-list'),
            self.employee_already_registered,
            content_type=self.content_type
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_can_list_employees(self):
        response = self.client.get(reverse('v1:employee-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_retrieve_employee(self):
        response = self.client.get(
            reverse('v1:employee-detail', args=[2]),
            content_type=self.content_type
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_delete_employee(self):
        response = self.client.delete(
            reverse('v1:employee-detail', args=[1]),
            content_type=self.content_type
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
