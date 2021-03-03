************
Installation
************

Django-vertical-multi-columns can be installed from PyPI with tools like ``pip``:

.. code-block:: bash

    pip install django-vertical-multi-columns

Add ``'vertical-multi-columns'`` to your ``INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'vertical-multi-columns',
    ]

You can specify a default number of columns in your Django settings:

.. code-block:: python

	VERTICAL_MULTI_COLUMNS = [
		{'NUMBER_OF_COLUMNS': 3}
	]

Django-vertical-multi-columns is tested against these versions of Python and `Django`__.

__ https://www.djangoproject.com/download/


* **Python**: 3.7, 3.8, 3.9
* **Django**: 2.2, 3.0, 3.1
