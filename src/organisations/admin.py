# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

try:
    from projects.models import Project
except ModuleNotFoundError:
    from bullet_train_api.projects.models import Project
from .models import Organisation


class ProjectInline(admin.StackedInline):
    model = Project
    extra = 0
    show_change_link = True


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    inlines = [
        ProjectInline
    ]
    list_display = ('__str__', )
    list_filter = ('projects', )
    search_fields = ('name', )
