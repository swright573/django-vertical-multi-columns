Django-Vertical-Multi-Columns
-----------------------------
Django-Vertical-Multi-Columns (VMC) is a reusable Django application allowing users
to display a list of items in side-by-side columns rather than in one long list.

|comparison|

Requirements
------------
* **Python**: 3.7, 3.8, 3.9
* **Django**: 2.2, 3.0, 3.1

Installation
------------
Install using pip:

.. code-block:: sh

    pip install vertical_multi_columns

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

**EvenView**
This view spreads your data across the number of columns you specify, keeping the length of the columns as even as possible.

|evenview|

**CriteriaView**
You provide a list of functions, one per column, that VMC uses to determine which column an item will be placed in.

|criteriaview|

**DefinedView**
You already have the columns you want displayed. You provide a column list and VMC does the rest.
 
|definedview|

Documentation
-------------
For more extensive document see the ``docs`` folder or `read it in readthedocs`_.

.. _`read it in readthedocs`: https://django-vertical-multi-columns.readthedocs.io/en/latest/index.html

Comments & Support
------------------
If you have questions about usage or development you can contact `Susan Wright`_ or open an issue on `GitHub`_.

Special Thanks
--------------

* To `Graham Wright`_ for his guidance and support in publishing this.

.. _`Susan Wright`: mailto:lsusanwright573@gmail.com
.. _`GitHub`: https://github.com/swright573/django-vertical-multi-columns/issues
.. _`Graham Wright`: https://github.com/gwright99/gwright99.github.io

.. |comparison| image:: https://user-images.githubusercontent.com/31971607/104608321-bbe9d100-564f-11eb-96ba-270fc192ef4b.gif
	:alt: Comparison

.. |evenview| image:: https://user-images.githubusercontent.com/31971607/104608352-c4daa280-564f-11eb-8084-2e78bf6ca1ce.gif
    :alt: EvenView
	
.. |criteriaview| image:: https://user-images.githubusercontent.com/31971607/104204473-51d8ee00-53fb-11eb-9824-11f835292ef4.gif
	:alt: CriteriaView
	
.. |definedview| image:: https://user-images.githubusercontent.com/31971607/104204480-53a2b180-53fb-11eb-91f9-98d624ccd170.gif
	:alt: DefinedView
