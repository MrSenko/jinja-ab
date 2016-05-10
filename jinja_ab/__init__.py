import os

from jinja2 import nodes
from jinja2.ext import Extension
from jinja2.exceptions import TemplateSyntaxError

_ENV = 'AB_EXPERIMENT'
_ENV_DEFAULT = 'control'


class JinjaAbExperimentExtension(Extension):
    """
        Jinja2 extension which supports the
        {% experiment <name> %} or {% ab <name> %} markup!
    """
    tags = set(['experiment', 'ab'])

    def parse(self, parser):
        opening_tag = parser.stream.current.value
        closing_tag = 'end' + opening_tag
        lineno = next(parser.stream).lineno

        # Parse the arguments
        while parser.stream.current.type != 'block_end':
            if parser.stream.current.test('name') or \
               parser.stream.current.test('string'):
                name = parser.stream.current.value
                next(parser.stream)
            else:
                raise TemplateSyntaxError("Can't parse experiment name",
                                          lineno)

        # Parse the contents of this tag
        body = parser.parse_statements(['name:%s' % closing_tag],
                                       drop_needle=True)

        # return the content matching the currently defined
        # JINJA_EXPERIMENT variable or empty string
        if os.environ.get(_ENV, _ENV_DEFAULT) == name:
            return body
        else:
            return nodes.Output([nodes.TemplateData(u'')])
