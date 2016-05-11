Jinja2 A/B testing extension
----------------------------

.. image:: https://img.shields.io/travis/MrSenko/jinja-ab/master.svg
   :target: https://travis-ci.org/MrSenko/jinja-ab
   :alt: Build status


This is an A/B testing extension for Jinja. It allows you to encode
experiments in your templates and renders the experiment selected by
the ``AB_EXPERIMENT`` environment variable. 'control' is the default
experiment name if ``AB_EXPERIMENT`` is not specified!

To install::

    pip install jinja-ab


Enable the extension in your code like this::

    import os
    import jinja_ab
    
    env = Environment(
            loader=FilesystemLoader(),
            extensions=[jinja_ab.JinjaAbExperimentExtension],
        )
    
    os.environ['AB_EXPERIMENT'] = 'v1'
    template = env.get_template('index.html')
    return template.render(context)

The template syntax is::

    {% experiment control %}This is the control{% endexperiment %}
    {% experiment v1 %}This is version 1{% endexperiment %}

Alternative syntax is also supported::

    {% ab control %}This is the control{% endab %}
    {% ab v1 %}This is version 1{% endab %}

You can also mix the two tags in a single template::

    {% experiment control %}This is the control{% endexperiment %}
    {% ab v1 %}This is version 1{% endab %}

Single and double quoted names are also supported!

**NOTE:** this extension deals with rendering the template string based
on the value of ``AB_EXPERIMENT``. It is up to you or your Jinja2 based tools
to decide what to do with the result. At `Mr. Senko <http://MrSenko.com>`_
we use this extension as part of the
`pelican-ab <https://github.com/MrSenko/pelican-ab>`_ plugin.

Contributing
============

Source code and issue tracker are at https://github.com/MrSenko/jinja-ab

Commercial support
==================

`Mr. Senko <http://MrSenko.com>`_ provides commercial support for open source
libraries, should you need it!
