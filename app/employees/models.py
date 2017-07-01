# ! coding: utf-8

from core import base
from django.db import models


class Employee(base.BaseModel):
    """The Employee Model"""

    email = models.EmailField(db_index=True, unique=True)

    name = models.CharField(max_length=255)

    department = models.CharField(max_length=255)

    class Meta:
        ordering = ['name', 'created_at']

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<{class_name} {self.name} from the {self.department} ({active_display})>'.format(
            class_name=self.__class__.__name__,
            self=self,
            active_display='Active' if self.is_active else 'Inative'
        )
