高级使用
=======

文件结构
-------
您可以用文件夹整理储存同类型的文档文件, 以保持清晰，可管理的文档结构。

以下是如何在文档中导入子文件夹中的``.rst`` 文件:

.. code:: rst
    .. toctree::
        usage
        /subdirectory/index
        api

在 ``index.rst`` 文件中, 将 ``.rst`` 文件名放在 ``.. toctree::`` 下,
它们就会呈现在您的文档中了。

子文件夹中的文件同样可以用路经的方式加入您的文档。

文档语言本土化
------------

添加其他语言可以通过创建一个新的Git项目, 然后在文档项目页, 点击 :guilabel:`⚙ 管理`, 然后选择对应的语言。

然后在 `主文档项目页 <https://readthedocs.org/projects/mza79-rtd-tutorial/>`_ 
点击 :guilabel:`⚙ 管理`, 再点击 :guilabel:`翻译`, 在project菜单中选择并加入新建的其他语言文档。
然后语言选择就会出现在文档页面左下角的弹出页面中了。

想了解更多语言本土化的信息, 请访问 `Read the Docs 官方文档 <https://docs.readthedocs.io/en/stable/localization.html>`_


