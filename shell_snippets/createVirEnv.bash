#!/usr/bin/env bash
# -*- coding: utf-8 -*-

cd project1/
pyenv which python
## /usr/bin/python
pyenv virtualenv <python_version> project1

pyenv local project1
python -V
## /home/#name/.pyenv/versions/project1/bin/python