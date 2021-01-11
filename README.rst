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


Why You May Need This
---------------------
Displaying a long list of items in a template is quite easy ... ``{% for row in rows %} ... {{ row.<field> }} ... {% endfor %}``. This comes at a cost for your end user though. Long lists 
can require someone who is looking for something to do a lot of paging up and down or jumping back and forth from page to page.

What VMC Does
-------------
VMC generates views with rows that contain multiple items where those items are still sorted so they can be read in order vertically but they are spread across the screen in side by side columns. 
You can specify the default number of columns in your Django settings. You can also override this by providing a different column setting in a VMC view. VMC views are sub-classes of ListView so all its capabilities are still available to you, such as pagination.

Impact on Templates
-------------------
Your template must account for the number of columns you ask for. The template coding is still fairly easy. Rather than ``{% for row in rows %} ... {{ row.<field> }} ... {% endfor %}`` you would 
code your template this way (for 3 columns):

.. code-block:: html

{% for row in rows %}
	<table>
	  <tr>
		<td>
            {% if row.0.<field> %}
                {{ row.0.<field>}}
            {%  endif %}
		</td>	
		<td>
            {% if row.0.<field> %}
                {{ row.0.<field>}}
            {%  endif %}
		</td>
		<td>
            {% if row.0.<field> %}
                {{ row.0.<field>}}
            {%  endif %}
		</td>
	  </tr>
	 </table> 
{% endfor %}

Note: The if statement is required because rows may have empty slots in situations where columns are of different lengths.

View Options
------------
There are 3 VMC views available.

EvenView
^^^^^^^^
Spreads your data across the number of columns you specify, keeping the length of the columns as even as possible.

CriteriaView
^^^^^^^^^^^^
You provide a list of functions, one per column, that VMC uses to determine which column an item will be placed in.

DefinedView
^^^^^^^^^^^
This is for the scenario where you already have columns that you want displayed as is. You provide the list and VMC does the rest.

Usage
-----

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

.. _`read the docs`: TBD
.. _`mailing list`: TBD

.. |comparison| image:: https://user-images.githubusercontent.com/31971607/104185855-90fb4500-53e3-11eb-87b2-ef301866de63.gif
	:alt: Comparison

.. |evenview| image:: https://user-images.githubusercontent.com/31971607/104191698-d754a200-53eb-11eb-8e77-374b58143567.gif
    :alt: EvenView
	
.. |criteriaview| image:: https://user-images.githubusercontent.com/31971607/104191709-db80bf80-53eb-11eb-8cae-cd182c92970c.gif
	:alt: CriteriaView
	
.. |definedview| image:: https://user-images.githubusercontent.com/31971607/104191740-e2a7cd80-53eb-11eb-90f2-b1fbb4331f1b.gif
	:alt: DefinedView
