from django.test import TestCase

try:
    from environments.models import Environment
    from organisations.models import Organisation
    from projects.models import Project
except ModuleNotFoundError:
    from bullet_train_api.environments.models import Environment
    from bullet_train_api.organisations.models import Organisation
    from bullet_train_api.projects.models import Project

from .models import Feature, FeatureState


class FeatureTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.organisation = Organisation.objects.create(name="Test Org")
        cls.project = Project.objects.create(name="Test Project", organisation=cls.organisation)
        cls.environment_one = Environment.objects.create(name="Test Environment 1",
                                                         project=cls.project)
        cls.environment_two = Environment.objects.create(name="Test Environment 2",
                                                         project=cls.project)

    def test_feature_should_create_feature_states_for_environments(self):
        feature = Feature.objects.create(name="Test Feature", project=self.project)

        feature_states = FeatureState.objects.filter(feature=feature)

        self.assertEquals(feature_states.count(), 2)

    def test_creating_feature_with_initial_value_should_set_value_for_all_feature_states(self):
        feature = Feature.objects.create(name="Test Feature", project=self.project,
                                         initial_value="This is a value")

        feature_states = FeatureState.objects.filter(feature=feature)

        for feature_state in feature_states:
            self.assertEquals(feature_state.get_feature_state_value(), "This is a value")
