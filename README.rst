=============================
Django-Vertical-Multi-Columns
=============================
|build| |docs| |codecov| |pypi| |pyvers| |licence| |black|

Django-Vertical-Multi-Columns (VMC) is a reusable Django application allowing you to easily display a list of items in vertically sorted side-by-side columns rather than in one long list. It supports all JSON data types ... string, number, boolean, object, array, and null/empty.

.. |build| image:: https://img.shields.io/github/workflow/status/swright573/django-vertical-multi-columns/lint-test/main
.. |docs|  image:: https://readthedocs.org/projects/pip/badge/
.. |codecov|  image:: https://codecov.io/gh/swright573/django-vertical-multi-columns/branch/main/graph/badge.svg
				:target: https://codecov.io/gh/swright573/django-vertical-multi-columns
.. |pypi|  image:: https://badge.fury.io/py/django-vertical-multi-columns.svg
    				:target: https://badge.fury.io/py/django-vertical-multi-columns
.. |pyvers|  image:: https://img.shields.io/pypi/pyversions/django-vertical-multi-columns
.. |licence|  image:: https://img.shields.io/badge/License-BSD%202--Clause-orange.svg
				:target: https://opensource.org/licenses/BSD-2-Clause
.. |black|  image:: https://img.shields.io/badge/code%20style-black-000000.svg
				:target: https://github.com/psf/black

|comparison|

Requirements
------------
* **Python**: 3.7, 3.8, 3.9
* **Django**: 2.2, 3.0, 3.1

Installation
------------
Install using pip:

.. code-block:: sh

    pip install django-vertical-multi-columns

Add 'vertical_multi_columns' to your INSTALLED_APPS setting.

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'vertical_multi_columns',
    ]

In your Django settings, you can optionally specify a default number of columns to be generated.

.. code-block:: python

	VERTICAL_MULTI_COLUMNS = [
		{NUMBER_OF_COLUMNS=3}
	]

Why You May Need This
---------------------
Displaying a long list of items in a template is quite easy.

``{% for row in rows %} ... {{ row.<field> }} ... {% endfor %}``

This comes at a cost for your end user though. Searching through a long list can test someone's patience if it requires a lot of scrolling or paging.

What VMC Does
-------------
* VMC views let you generate rows that can easily be displayed in multiple side-by-side columns in your templates. The columns retain your sort order so your users can still scan the data in a natural up-and-down way. And because the items are spread across the screen, your content takes  less vertical space, reducing the amount of scrolling/paging a user must do.
* You specify the number of columns you want generated.
* VMC views are sub-classes of ListView so all its capabilities are still available to you.

View Options
------------
There are 3 views available.

**EvenView** spreads your data across the number of columns you specify, keeping the length of the columns as even as possible.

|evenview|

**CriteriaView** lets you provide a list of functions, one per column, that VMC uses to determine which column an item will be placed in.

|criteriaview|

**DefinedView** lets you provide the columns you want displayed. VMC does the rest.

|definedview|

Documentation
-------------
For more extensive document see the ``docs`` folder or read it in `readthedocs`_.

.. _`readthedocs`: https://django-vertical-multi-columns.readthedocs.io/en/latest/index.html

Comments & Support
------------------
If you have questions about usage or development you can open an issue on `GitHub`_.  You can also contact `Susan Wright`_ directly.

Special Thanks
--------------

* To `Graham Wright`_ for his guidance and support in publishing this.

.. _`Susan Wright`: mailto:lsusanwright573@gmail.com
.. _`GitHub`: https://github.com/swright573/django-vertical-multi-columns
.. _`Graham Wright`: https://github.com/gwright99/gwright99.github.io

.. |comparison| image:: https://user-images.githubusercontent.com/31971607/106627777-21422b00-6547-11eb-9a8a-49b50d826dc0.jpg
	:alt: Comparison

.. |evenview| image:: https://user-images.githubusercontent.com/31971607/106627791-269f7580-6547-11eb-80ca-6737b5792d63.GIF
    :alt: EvenView

.. |criteriaview| image:: https://user-images.githubusercontent.com/31971607/106650000-59a23300-6560-11eb-8c2e-10b617db92af.GIF
	:alt: CriteriaView

.. |definedview| image:: https://user-images.githubusercontent.com/31971607/106651467-2d87b180-6562-11eb-9c36-0e696a0e9b8c.GIF
	:alt: DefinedView
