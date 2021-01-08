Django-Vertical-Multi-Columns
-----------------------------

Django-Vertical-Multi-Columns (VMC) is a reusable Django application allowing users
to display a list of items in side-by-side columns rather than in one long list.

This

.. image:: https://github.com/swright573/django-vertical-multi-columns/blob/main/docs/images/multiplecolumns.gif
   :width: 704
   :alt: Multiple columns

![Screenshot](/docs/images/multiplecolumns.gif?raw=true "Susan") 


rather than this

.. image:: https://github.com/swright573/django-vertical-multi-columns/docs/images/singlecolumn.gif
   :width: 161
   :alt: Single column

![Screenshot] (https://github.com/swright573/django-vertical-multi-columns/docs/images/singlecolumn.gif)   

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