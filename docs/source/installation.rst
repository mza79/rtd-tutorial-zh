Installation
============

Clone the repository from `Git Hub <https://github.com/mza79/rtd-tutorial>`_ in your local file.
And you are ready to edit the docs.

Configuring Project
-------------------

In the build configuration file ``conf.py``, you can edit the configuration
to customize Sphinx input and output behavior.

project
"""""""
    The document project name

author
""""""
    the author name(s)

copyright
"""""""""
    A copyright statement in the style '2008, Author Name'.

version
"""""""
    The major project version, eg. for python, the verison may be 3.8

release
""""""
    The full project version, eg. for python, the release may be 3.8.3

.. code-block:: python

    project = 'How to Use Read the Docs Documentation '
    copyright = '2022,Tom Zhang'
    author = 'Tom Zhang'

    release = '0.1'
    version = '0.1.0'


You can add and enable extensions to your project by adding the extension name
to the extension's list

.. code-block:: python

   extensions = [
        ... ,
        'new-extension',
    ]

For more detailed documentation you can visit the `sphinx page <https://www.sphinx-doc.org/en/master/usage/configuration.html>`_

Configuring Read the Docs Build
-------------------------------

You can configure the build of your documentaion in ``.readthedocs.yaml``

version
"""""""

verision of the configuration file ``.readthedocs.yaml``

Example

.. code-block:: yaml
    version: 2

If version not provided, version 1 (deprecated) will be used.

build
"""""

Configuration for the documentation build process. 
**os** field allows you to specify the base Read the Docs image used 
to build the documentation. 
**tools** field allows you to control the versions of 
several tools: Python, Node.js, Rust, and Go.
**jobs** field allows you to configure commands to run before/after 
the documentaion build.

Example

.. code-block:: yaml

    build:
        os: "ubuntu-20.04"
        tools:
            python: "3.8"
    jobs:
        pre_create_environment:
        - echo "Command run at 'pre_create_environment' step"
        post_build:
        - echo "Command run at 'post_build' step"
        - echo `date`

python
""""""

Configuration of the Python environment to be used.

.. code-block:: yaml

    verision: 2
    python:
        install:
            - requirements: docs/requirements.txt
            - method: pip
            path: .
            extra_requirements:
                - docs
            - method: setuptools
            path: another/package
        system_packages: true

Example

.. code-block:: yaml

    build:
        os: "ubuntu-20.04"
        tools:
            python: "3.8"

sphinx
""""""

Configuration for Sphinx documentation (this is the default documentation type).

.. code-block:: yaml

    version: 2

    sphinx:
        builder: html
        configuration: conf.py
        fail_on_warning: true

formats
"""""""

Additional formats of the documentation to be built, apart from the default HTML.

Example

.. code-block:: yaml

    formats:
        - pdf
        - epub

This section is referenced from `Read the Docs Documentation <https://docs.readthedocs.io/en/stable/config-file/index.html>`_
and for more information, you can visit the `Read the Docs Documentation <https://docs.readthedocs.io/en/stable/config-file/index.html>`_