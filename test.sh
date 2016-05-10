#!/bin/bash

flake8 jinja_ab/ && \
coverage run --source jinja_ab/ --branch -m unittest -v jinja_ab.tests && \
coverage report -m
