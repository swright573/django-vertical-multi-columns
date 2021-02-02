*****
Usage
*****

There are 3 VMC views available. They are all subclasses of Django's ListView so in addition to the specific VMC capabilities described below, all ListView's capabilities are still available to you.

View Options
------------

**EvenVMCView** 

Spreads your data across the number of columns you specify, keeping the columns pretty much the same length.

|evenview|

**CriteriaVMCView** 

You provide a list of functions, one per column. VMC uses these to determine in which column an item should be placed.

|criteriaview|

**DefinedVMCView** 

You already have the columns you want displayed. You provide the column list and VMC does the rest.
 
|definedview|

Setting the Number of Columns
-----------------------------

There are several ways to specify how many columns should be used in your VMC views. In priority order:

1. Pass kwarg ``num_columns`` to ``super().__init__()`` in your VMC view's ``__init__()``.

.. code-block:: python

    def __init__(self):
        super().__init__(num_columns=5)

2. In your Django settings, specify a default number of columns to be generated. This is overridden if you pass a num_columns kwarg.

.. code-block:: python

	VERTICAL_MULTI_COLUMNS = [
		{NUMBER_OF_COLUMNS=3}
	]

3. If you there is not setting and you don't pass a num_columns kwarg, the number of columns defaults to 3 .

Required Method Overrides
-------------------------

You must override some methods in the VMC classes.

**EvenVMCView**: Define a method:

* ``get_data()`` that returns a list of sorted data in JSON format.
	
**CriteriaVMCView**: Define 2 methods:

* ``get_data()`` that returns a list of sorted data in JSON format.

* ``get_column_criteria()`` that returns two things:

	* a list of the functions VMC should use to place your data items into each column.
	* a list of the dictionary keys referenced in the functions.
	
	* NOTE: See How Passed CriteriaVMCView Functions Work below for a more in depth explanation.
	 
**DefinedVMCView**: Define a method:

* ``get_data()`` to return a list of pre-defined columns in JSON formaton. The number should correspond to the number of columns specified.

Sample Code
-----------

This example implements EvenVMCView but they are all fairly similar. Differences are noted below. Note that the example is pulling API data via requests but data from any source can be used.

.. code-block:: python

    from vertical_multi_columns.configure import EvenVMCView
    import requests


.. code-block:: python

	class MyEvenView(EvenVMCView):
	    def __init__(self, **kwargs):
            #You can pass an optional num_columns kwarg to override
            #    the value in settings.
            # If there is nothing in settings and you don't pass
            #    num_columns, the number of columns will be 3.
            super().__init__(num_columns=5)

        def get_data(self):
            # Write logic to retrieve the data to be displayed (often from an API)
            # Sort it appropriately
            # Note that data must be in JSON format.
            resp = requests.get(<api_url>)
            raw_api_data = resp.json()
            sorted_api_data = sorted(raw_api_data, key=lambda i: i['<field>'])
            return sorted_api_data

        template_name = '<your_template>.html'
        context_object_name = "<your_choice>"

When is a VMC View Appropriate?
-------------------------------

VMC views are meant for situations where you want to display a lots of short data in less vertical space than a straightforward ListView would require.

A common use case is to query an API for a list of choices (e.g. a list of plants or a list of car models) which you display as links in a VMC view. The end user could select one of those links which triggers a further call to the API to retrieve more detailed information about that choice. You could display that in a DetailView.

While VMC views do support hierarchical JSON data, this is not recommended since it adds unneeded complexity to your Django templates. You are better off either:

* limiting your "VMC" API return data to only what is required for a user to make a choice, or
* if hierarchical JSON must be returned by the API, extract the data you need in the view.

.. _how-passed-functions-work:

How Passed CriteriaVMCView Functions Work
-----------------------------------------

You pass a list of functions and a list of your data's JSON keys to CriteriaVMCView to determine in which column each data item should appear. This scenario should help explain how you write those functions.

Scenario:

Your API call returns a set of data which includes a list of plants. Specifically the data contains 'name' and 'id'. If required, the data has been converted to JSON format.

``[{'id': 5, 'name': 'Asparagus'}, {'id': 2, 'name': 'Basil'}, ...  , {'id': 34, 'name': 'Winter Squash'}]``

Say you want to display 3 columns ... plants starting with A-F in one column, those starting with G-S in another, and T-Z in a third column.

We'll use A-F as an example. It would be included in the function list (one per column) you pass to CriteriaVMCView in your get_column_criteria() method. This function is looking for instances in your returned data where the first letter of 'name' is in the range 'ABCDEF'. If so, the function returns True. If not, it returns False.

.. code-block:: python

    def a_to_f(self, args):
        parms = args.split(",")
        return 'ABCDEF'.find(parms[0][0]) > -1

In get_column_criteria(), you will also pass a list of the JSON keys ``['name']`` you want to query in a function. In this case, you only want to query 'name'.

CriteriaVMCView's logic will apply your functions to each item in your data to determine if that item should appear in that function's column. A function might use only some of the JSON keys you pass. You must also 

Say the data item being processed is ``{'id': 5, 'name': 'Asparagus'}``. The 'args' passed to the a_to_f function will be string ``'Asparagus, 5'`` since we said our keys were ``['name', 'id']``.

The passed string will be split by our function, giving list ``['Asparagus', '5']``.

Since our function is only interested in the name, it looks only at ``parms[0]`` which is 'Asparagus'. And further, since it is only interested in the first letter of name, it only looks at ``parms[0][0]`` which is 'A'. The function returns True if parms[0][0] is in the range A-F and False if it is not.

If True, that item will appear in the column. If False, it will not. Note that items can appear in multiple columns if function criteria overlap. Conversely an item can appear in no columns if none of the function criteria are met.

How to Contact/Get Support
--------------------------

If you have questions about usage or development you can participate in the discussion or open an issue on `GitHub`_.  You can also contact `Susan Wright`_ directly.

.. _`Susan Wright`: mailto:lsusanwright573@gmail.com
.. _`GitHub`: https://github.com/swright573/django-vertical-multi-columns

.. |evenview| image:: https://user-images.githubusercontent.com/31971607/106627791-269f7580-6547-11eb-80ca-6737b5792d63.GIF
    :alt: EvenView
	
.. |criteriaview| image:: https://user-images.githubusercontent.com/31971607/106650000-59a23300-6560-11eb-8c2e-10b617db92af.GIF
	:alt: CriteriaView
	
.. |definedview| image:: https://user-images.githubusercontent.com/31971607/106651467-2d87b180-6562-11eb-9c36-0e696a0e9b8c.GIF
	:alt: DefinedView