# ! coding: utf-8

from django.db import models
from django.db.models import manager


class BaseQuerySet(manager.QuerySet):
    """Base Queryset for all models."""

    _only_actives_records = True

    def _clone(self, **kwargs):
        clone = super(BaseQuerySet, self)._clone(
            _only_actives_records=self._only_actives_records, **kwargs)
        if self._only_actives_records:
            clone.query.add_q(models.Q(is_active=True))
        return clone

    def all_actives_and_inatives(self):
        self._only_actives_records = False
        return self.all()

    def inatives(self):
        return self.all_actives_and_inatives().filter(is_active=False)

BaseManager = manager.Manager.from_queryset(BaseQuerySet)


class BaseModel(models.Model):

    objects = BaseManager()

    is_active = models.BooleanField(default=True, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']
