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

    pip install vertical_multi_columns

Then add ``'vertical_multi_columns'`` to your ``INSTALLED_APPS``.

.. code-block:: python

    INSTALLED_APPS = [
        ...
        'vertical_multi_columns',
    ]
	
You can specify a default number of columns in your Django settings:

.. code-block:: python

	VERTICAL_MULTI_COLUMNS = [
		{NUMBER_OF_COLUMNS=3}
	]	

Why You May Need This
---------------------
Displaying a long list of items in a template is quite easy ... ``{% for row in rows %} ... {{ row.<field> }} ... {% endfor %}``. This comes at a cost for your end user though. Long lists 
can require someone who is looking for something to do a lot of scrolling up and down or jumping back and forth from page to page.

What VMC Does
-------------
VMC generates views with rows that contain multiple items where those items are still sorted so they can be read in order vertically but they are spread across the screen in side by side columns. 
You can specify the default number of columns in your Django settings. You can also override this by passing a different column setting to a VMC view. VMC views are sub-classes of ListView so all its capabilities are still available to you.

View Options
------------
There are 3 VMC views available.

**EvenView** Spreads your data across the number of columns you specify, keeping the length of the columns as even as possible.

|evenview|

**CriteriaView** You provide a list of functions, one per column, that VMC uses to determine which column an item will be placed in.

|criteriaview|

**DefinedView** You already have the columns you want displayed. You provide a column list and VMC does the rest.
 
|definedview|

Support
-------

If you have questions about usage or development you can ... <tbd>

.. _`read the docs`: TBD
.. _`mailing list`: TBD

.. |comparison| image:: https://user-images.githubusercontent.com/31971607/104185855-90fb4500-53e3-11eb-87b2-ef301866de63.gif
	:alt: Comparison

.. |evenview| image:: https://user-images.githubusercontent.com/31971607/104204457-4eddfd80-53fb-11eb-9d0d-06db9dafb5c8.gif
    :alt: EvenView
	
.. |criteriaview| image:: https://user-images.githubusercontent.com/31971607/104204473-51d8ee00-53fb-11eb-9824-11f835292ef4.gif
	:alt: CriteriaView
	
.. |definedview| image:: https://user-images.githubusercontent.com/31971607/104204480-53a2b180-53fb-11eb-91f9-98d624ccd170.gif
	:alt: DefinedView
