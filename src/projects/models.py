# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

try:
    from organisations.models import Organisation
except ModuleNotFoundError:
    from bullet_train_api.organisations.models import Organisation


class Project(models.Model):
    name = models.CharField(max_length=2000)
    created_date = models.DateTimeField('DateCreated', auto_now_add=True)
    organisation = models.ForeignKey(
        Organisation,
        related_name='projects',
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ['id']
        unique_together = ('name', 'organisation')

    def __str__(self):
        return "Project %s" % self.name
