基础使用
=======

编写内容
-------
在 ``/docs/`` 目录下, 用GitHub自带的编辑功能或者您最爱的编辑器打开您想要编辑的 ``.rst`` 文件。

写入一些内容, 然后保存, 提交, 推入Git仓库。对, 就是这么简单。

查看您的更改
----------
开发环节中最重要的，就是开发进程的可视化。

在您提交你的更改到GiiHub后, 访问 `文档构建页面 <https://readthedocs.org/projects/mza79-rtd-tutorial/builds/>`_ 查看构建状态。 
构建成功后, 您可以点入完成的构建页面，然后点击右上的 :guilabel:`查看文档` , 就可以查看您的文档了。

如何写标题
----------

章段标题:

.. code-block::

   这就是章段标题
   ============

部分标题:

.. code-block::

   ############
   这就是部分标题
   ############

以及其他的标题种类:

* # 用于部分标题, 上下两层。
* \* 用于章节标题, 上下两层。
* = 用于章段标题， 下面一层。
* \- 用于小节标题
* ^ 用于小小节标题
* " 用于自然段标题


如何写列表
---------
这是个列表
   * 这个是列表项
   * 这又是列表项
      * 这是嵌套列表项
   1. 这是编号列项
   2. 这是编号列项
   #. 这也是编号列项
   #. 这还是编号列项

.. code-block:: 

   这是个列表
      * 这个是列表项
      * 这又是列表项
         * 这是嵌套列表项
      1. 这是编号列项
      2. 这是编号列项
      #. 这也是编号列项
      #. 这还是编号列项


如何写备注
----------
.. note:: 
   备注就是这长个样子的
   
   | .. note::
   |      加上上面这行就可以写备注了

小提示
---------------
.. tip::
   小提示就是长这个样子的:

        | .. tip:: 
        |   加上上面这行就可以写提示了

如何导入图片
----------
你可以用以下代码导入图片:

.. image:: ../Media/Images/beautiful-image.jpg
   :width: 80%
   :align: center
   :alt: this is a beautiful image

.. code-block:: RST
  
    .. image:: ../Media/Images/beautiful-image.jpg
        :width: 80%
        :align: center
        :alt: this is a beautiful image


加入更多文体
----------

粗体
^^^^
文本包裹的像 \*\*这样\*\* 就是 **粗体**.

斜体
^^^^^^
文本包裹的像  \*这样\* 就是 *斜体*.

代码样式
^^^^^^
文本包裹的像 \`\`这样\`\` 就是 ``代码样式``.

文字块
^^^^^^^^^^^^^^
您可以用以下代码加入文字块: 

.. code-block:: rst

   .. code-block::
   这是文字块

标签
^^^^
这是一个 :guilabel:`标签`, 可以用以下代码使用

.. code-block:: 

   This is a :guilabel:`Label`

链接
^^^^
这是一个指向 `文档首页 <https://mza79-rtd-tutorial.readthedocs.io/en/stable/index.html>`_ 的链接。

.. code-block::

   这是一个指向 `文档首页 <https://mza79-rtd-tutorial.readthedocs.io/en/stable/index.html>`_ 的链接。


专业术语
^^^^^^^
您可以在词汇表页面中加入专业术语的定义, 词汇表由以下代码声明:
``.. glossary::``

这是一个 :term:`专业术语`, 可以用以下代码使用:

.. code-block::

   :term:`专业术语`

