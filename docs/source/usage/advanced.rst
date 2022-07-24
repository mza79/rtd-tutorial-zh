Advanced usage
==============

File Structuring
----------------
You can structure and organize your documentations files using file
structures.

And here's how you organize ``.rst`` files into your documentation page:

.. code:: rst
    .. toctree::
        .rst file 1
        /subdirectory/index
        .rst file 2

In your ``index.rst``, add ``.rst`` files under ``.. toctree::``, then they will appear
as a child page of your index page.

You can also organize sections of documentaion into subdirectories and you can
add them to your doc tree as well.

Localization of Documentation
------------------------------
WIP

