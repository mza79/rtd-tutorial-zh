如何安装
=======

从 `Git Hub <https://github.com/mza79/rtd-tutorial>`_ 将源文件下载到您的本地文件,
然后您就可以开始编辑这个文档了。

项目配置
-------

在构建配置文件（ ``conf.py`` ）中， 您可以自定义Sphinx的输入和输出行为。


project
"""""""
    文档项目名称。

author
""""""
    作者的名字。

copyright
"""""""""
    版权宣言，格式如： '2008, 作者名'。

version
"""""""
    项目版本号, 列： 以Python为例, 版本号可以是 3.8.3。

release
"""""""

    项目发布版本号, 以Python为例, 它的发布版本号可以是 3.8

.. code-block:: python

    project = 'How to Use Read the Docs Documentation '
    copyright = '2022,Tom Zhang'
    author = 'Tom Zhang'

    release = '0.1'
    version = '0.1.0'

您可以通过在extension列表中加入插件名 以启用和添加插件到您的文档中。

.. code-block:: python

   extensions = [
        ... ,
        'new-extension',
    ]

想要阅读更详细的文档，您可以访问 `Sphinx page <https://www.sphinx-doc.org/en/master/usage/configuration.html>`_

配置Read the Docs的构建
----------------------

您可以在 ``.readthedocs.yaml`` 文件中配置文档的构建。

version
"""""""

verision 参数指定了在 ``.readthedocs.yaml`` 文件中使用的版本 

例

.. code-block:: yaml
    version: 2

如果没有定义版本的话, 默认会使用版本1(旧). 

build
"""""
配置文档的构建过程

**os**  参数可以让您指定Read the Docs构建中使用的基础镜像。
| **tools**  参数可以让您设置使用的编程语言以及版本: Python, Node.js, Rust, and Go。
| **jobs**  参数可以让您自定义文档在构建开始前和结束后执行的命令。

例

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

设置构建中的Python环境

例

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

sphinx
""""""

Sphinx 的设置 (Sphinx是默认使用的文档语言).

.. code-block:: yaml

    version: 2

    sphinx:
        builder: html
        configuration: conf.py
        fail_on_warning: true

formats
"""""""
设置除了默认html以外构建的格式: pdf, epub

Example

.. code-block:: yaml

    formats:
        - pdf
        - epub

这个分段参考了 `Read the Docs 官方文档 <https://docs.readthedocs.io/en/stable/config-file/index.html>`_
想了解更多？ 您可以访问 `Read the Docs 官方文档 <https://docs.readthedocs.io/en/stable/config-file/index.html>`_ 