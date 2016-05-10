import os
import jinja_ab
from unittest import TestCase
from jinja2 import Environment
from jinja2.loaders import DictLoader
from jinja2.exceptions import TemplateSyntaxError


class JinjaAbTestCase(TestCase):
    def tearDown(self):
        "Clean-up the environment"
        if jinja_ab._ENV in os.environ:
            del os.environ[jinja_ab._ENV]

    def _render(self, loader, context={}):
        "Helper method"
        env = Environment(
                loader=loader,
                extensions=[jinja_ab.JinjaExperimentExtension],
            )
        template = env.get_template('index.html')
        return template.render(context).strip()

    def test_without_experiment_tags(self):
        """
            WHEN experiment tags are missing,
            THEN rendering still works
        """
        loader = DictLoader({'index.html': 'Hello World'})
        self.assertEquals(self._render(loader), 'Hello World')

    def test_with_experiments_and_no_env(self):
        """
            WHEN AB_EXPERIMENT is not specified,
            THEN the control experiment is returned
        """
        loader = DictLoader({'index.html': """
{% experiment control %}This is the control{% endexperiment %}
{% experiment v1 %}This is version 1{% endexperiment %}
"""})
        self.assertEquals(self._render(loader), 'This is the control')

    def test_with_experiments_and_env(self):
        """
            WHEN AB_EXPERIMENT is specified,
            THEN only that particular experiment is returned
        """
        loader = DictLoader({'index.html': """
{% experiment control %}This is the control{% endexperiment %}
{% experiment v1 %}This is version 1{% endexperiment %}
"""})
        os.environ[jinja_ab._ENV] = 'v1'
        self.assertEquals(self._render(loader), 'This is version 1')

    def test_with_experiment_name_in_single_quotes(self):
        """
            WHEN experiment name is quoted,
            THEN rendering works as well
        """
        loader = DictLoader({'index.html': """
{% experiment 'control' %}This is the control{% endexperiment %}
{% experiment "v1" %}This is version 1{% endexperiment %}
"""})
        self.assertEquals(self._render(loader), 'This is the control')

    def test_with_experiment_name_in_double_quotes(self):
        """
            WHEN experiment name is quoted,
            THEN rendering works as well
        """
        loader = DictLoader({'index.html': """
{% experiment 'control' %}This is the control{% endexperiment %}
{% experiment "v1" %}This is version 1{% endexperiment %}
"""})
        os.environ[jinja_ab._ENV] = 'v1'
        self.assertEquals(self._render(loader), 'This is version 1')

    def test_with_experiment_name_which_is_variable(self):
        """
            WHEN experiment name is not a name or string,
            THEN invalid syntax error is returned
        """
        loader = DictLoader({'index.html': """
{% set my_experiment = 'control' %}
{% experiment {{ my_experiment }} %}This is the control{% endexperiment %}
"""})
        with self.assertRaises(TemplateSyntaxError):
            self._render(loader)
