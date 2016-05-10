Jinja2 A/B testing extension
----------------------------

.. image:: https://img.shields.io/travis/MrSenko/jinja-ab/master.svg
   :target: https://travis-ci.org/MrSenko/jinja-ab
   :alt: Build status


This is an A/B testing extension for Jinja. It allows you to encode
experiments in your templates and renders the experiment selected by
the `AB_EXPERIMENT` environment variable. 'control' is the default
experiment name if `AB_EXPERIMENT` is not specified! The syntax is::

    {% experiment control %}This is the control{% endexperiment %}
    {% experiment v1 %}This is version 1{% endexperiment %}

Single and double quoted names are also supported.

**NOTE:** this extension deals with rendering the template string based
on the value of `AB_EXPERIMENT`. It is up to you or your Jinja2 based tools
to decide what to do with the result.

Contributing
============

Source code and issue tracker are at https://github.com/MrSenko/jinja-ab
