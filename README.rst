Manifold
========

Call any type of genomic variant using zero or more reference sequences.

Current version: 0.0.9

Installation
------------

::

    pip install .


Development
-----------

To do development in this codebase, the python3 development package must be installed.

After installation the Manifold development environment can be set up by the
following commands:

::

    python3 -mvenv venv
    . venv/bin/activate
    pip install -r dev-requirements.txt
    pip install -e .

Linting files
`````````````

::

    # run all linting commands
    tox -e lint

    # reformat all project files
    black src tests setup.py

    # sort imports in project files
    isort -rc src tests setup.py

    # check pep8 against all project files
    flake8 src tests setup.py

    # lint python code for common errors and codestyle issues
    pylint src


Tests
`````

::

    # run all linting and test
    tox

    # run only (fast) unit tests
    tox -e unit

    # run only linting
    tox -e lint

