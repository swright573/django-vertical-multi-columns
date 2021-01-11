Django-Vertical-Multi-Columns
-----------------------------

Django-Vertical-Multi-Columns (VMC) is a reusable Django application allowing users
to display a list of items in side-by-side columns rather than in one long list.

|comparison|

Requirements
------------

* **Python**: 3.5, 3.6, 3.7, 3.8, 3.9
* **Django**: 2.2, 3.0, 3.1


Installation
------------

Install using pip:

.. code-block:: sh

    pip install vertical-multi-columns

Then add ``'vertical_multi_columns'`` to your ``INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'vertical_multi_columns',
    ]


Usage
-----

Displaying a long list of data in a template is quite easy ... {% for row in rows %} ... {% endfor %}.

What VMC does is generate "rows" that contain multiple items where the

Django-filter can be used for generating interfaces similar to the Django
admin's ``list_filter`` interface.  It has an API very similar to Django's
``ModelForms``.  For example, if you had a Product model you could have a
filterset for it with the code:

.. code-block:: python

    import vertical_multi_columns


And then in your view you could do:

.. code-block:: python

    def




Support
-------

If you have questions about usage or development you can join the
`mailing list`_.

.. _`read the docs`: https://django-filter.readthedocs.io/en/master/
.. _`mailing list`: http://groups.google.com/group/django-filter

.. |comparison| image:: https://user-images.githubusercontent.com/31971607/104185855-90fb4500-53e3-11eb-87b2-ef301866de63.gif

.. |multiple-columns-small| image:: https://user-images.githubusercontent.com/31971607/104095425-b6ae1000-5264-11eb-96c2-bf9b2542de6d.gif
    :alt: Multiple Columns
	:width: 352px
	:height: 119px
	:align: top
	
.. |single-column-small| image:: https://user-images.githubusercontent.com/31971607/104095428-bada2d80-5264-11eb-813d-e3e7e04c587c.gif
	:alt: Single Columns
	:width: 68 px
	:height: 368px
	:align: top