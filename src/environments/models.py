# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _

from app.utils import create_hash
from django.utils.encoding import python_2_unicode_compatible
from features.models import FeatureState
from projects.models import Project


@python_2_unicode_compatible
class Environment(models.Model):
    name = models.CharField(max_length=2000)
    created_date = models.DateTimeField('DateCreated', auto_now_add=True)
    project = models.ForeignKey(
        Project,
        related_name="environments",
        help_text=_(
            "Changing the project selected will remove all previous Feature States for the "
            "previously associated projects Features that are related to this Environment. New "
            "default Feature States will be created for the new selected projects Features for "
            "this Environment."
        ),
        on_delete=models.CASCADE,
    )
    api_key = models.CharField(default=create_hash, unique=True, max_length=100)

    class Meta:
        ordering = ['id']

    def save(self, *args, **kwargs):
        """
        Override save method to initialise feature states for all features in new environment
        """
        requires_feature_state_creation = True if not self.pk else False
        if self.pk:
            old_environment = Environment.objects.get(pk=self.pk)
            if old_environment.project != self.project:
                FeatureState.objects.filter(
                    feature__in=old_environment.project.features.values_list('pk', flat=True),
                    environment=self,
                ).all().delete()
                requires_feature_state_creation = True

        super(Environment, self).save(*args, **kwargs)

        if requires_feature_state_creation:
            # also create feature states for all features in the project
            features = self.project.features.all()
            for feature in features:
                FeatureState.objects.create(
                    feature=feature,
                    environment=self,
                    identity=None,
                    enabled=feature.default_enabled
                )

    def __str__(self):
        return "Project %s - Environment %s" % (self.project.name, self.name)


@python_2_unicode_compatible
class Identity(models.Model):
    identifier = models.CharField(max_length=2000)
    created_date = models.DateTimeField('DateCreated', auto_now_add=True)
    environment = models.ForeignKey(
        Environment,
        related_name='identities',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = "Identities"
        ordering = ['id']

    def get_all_feature_states(self):
        # get all features that have been overridden for an identity
        identity_flags = self.identity_features.filter(identity=self)

        override_features = [flag.feature for flag in identity_flags]

        # get only feature states for features which are not associated with an identity
        # and are not in the to be overridden generated above
        environment_flags = self.environment.feature_states.filter(environment=self.environment,
                                                                   identity=None)\
            .exclude(feature__in=override_features)

        return identity_flags, environment_flags

    def __str__(self):
        return "Account %s" % self.identifier
