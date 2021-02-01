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

You provide a list of functions, one per column, used by VMC to determine in which column an item should be placed.

|criteriaview|

**DefinedVMCView** 

You already have the columns you want displayed. You provide a column list and VMC does the rest.
 
|definedview|

Setting the Number of Columns
-----------------------------

There are several ways to specify how many columns should be used in your VMC views. In priority order:

1. Pass kwarg ``num_columns`` to super().__init__().

..code-block:: python

    def __init__(self):
        super().__init__(num_columns=5)

2. In your Django settings, specify a default number of columns to be generated. This is overridden if you pass a num_columns kwarg.

.. code-block:: python

	VERTICAL_MULTI_COLUMNS = [
		{NUMBER_OF_COLUMNS=3}
	]

3. If you there is not setting and you don't pass a num_columns keyword argument, the number of columns defaults to 3 .

Required Method Overrides
-------------------------

You must override some methods in the VMC classes so you can define what and how data will be displayed.

**EvenVMCView**

Define a method:

* ``get_data()`` to return a list of sorted data to be displayed, returned in JSON format.
	
**CriteriaVMCView**

Define 2 methods:

* ``get_data()`` to return a list of sorted data to be displayed, returned in JSON format.

* ``get_column_criteria()`` to return two things:
	* a list containing the functions VMC should use to place your data items into columns, one function per column.
	* a list containing the dictionary keys referenced in the functions.
	* NOTE: See :ref:`How Passed CriteriaVMCView Functions Work` below for a more in depth explanation.
	 
**DefinedVMCView**

Define a method:
* ``get_data()`` to return a list of pre-defined columns in JSON format. The number of columns must correspond to the 

Sample Code
-----------

This example implements EvenVMCView but they are all fairly similar. Differences are noted below. Note that the example is pulling API data via requests but data from any source can be used.

.. code-block:: python

    from vertical_multi_columns.configure import EvenVMCView
	import requests


.. code-block:: python

	class MyEvenView(EvenVMCView):
		def __init__(self, **kwargs):
			# You can pass an optional num_columns kwarg to override
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

Example Site
------------

There is a example site you can install and run to see the VMC views in action. It has no external requirements other than for you to have pip installed
both Django itself and the django-vertical_multi_columns package.

(*Windows commands shown. Use the equivalent if you run on Mac or Linux.*)

1. Create a Python virtual directory and activate it. (*This is optional. If using, use your normal method.*)

.. code-block:: bash

	python -m venv <*virtualdirectory*>
	.\<*virtualdirectory*\scripts\activate

2. Install Django and the django-vertical-multi-columns package.

.. code-block:: bash

	pip install django
	pip install django-vertical-multi-columns

3. Create a new Django project called vmcexamplesite.

.. code-block:: bash

	django-admin startproject vmcexamplesite
	
4. Copy all the files in the directory *example-site* in the repo into the vmcexamplesite directory Django just created.

.. code-block:: bash

	cd .\vmcexamplesite
	copy <*repo_directory*>\example-site\*.*
	
5. Update settings.py with your secret key (*or use an environment variable*)

.. code-block:: bash

	SECRET_KEY = <*insert your Django secret key here*>

6. Execute runserver to activate the site.

.. code-block:: bash

	python manage.py runserver
	
7. Point your browser to localhost:8000. More information about the site is provided there under "About the VMC Example Site.

A Note about When a VMC View is Appropriate
-------------------------------------------

VMC views are meant for situations where you want to display a lot of short data in less vertical space than a straightforward ListView would require.

A common use case would be to query an API for a list of choices (e.g. a list of plants or a list of car models) which you display as links in a VMC view. The end user could select one of those choices which would trigger a further call to the API to retrieve more detailed information about that choice that you could display in a DetailView.

While VMC views (specifically EvenVMCView and CriteriaVMCView) do support hierarchical JSON data, it is not recommended since this adds unneeded complexity to your Django templates. You are better off either:

* limiting your "VMC" API call data to only what is required for a user to make a choice, or
* extracting from the returned API data only what you need for a user to make a choice and passing only that to the VMC view.

How Passed CriteriaVMCView Functions Work
-----------------------------------------

You pass a list of functions and a list of your data's JSON keys to CriteriaVMCView to determine in which column each data item should appear. This scenario should help explain how you should write those functions.

Scenario:

Your API call returns a set of data which includes a list of plants. Specifically the data contains 'name' and 'id'. If required, the data has been converted to JSON format.

.. code-block:: python

[{'id': 5, 'name': 'Asparagus'}, {'id': 2, 'name': 'Basil'}, ...  , {'id': 34, 'name': 'Winter Squash'}]

Say you want to display 3 columns ... plants starting with A-F in one column, those starting with G-S in another, and T-Z in a third column.

Using A-F as an example, in the function list (one per column) you pass to CriteriaVMCView when you override the get_column_criteria() method, you would pass this function . This function is looking for instances in your returned data where the first letter of 'name' is in the range 'ABCDEF'. If so, the function returns True. If not, it returns False.

.. code-block:: python

    def a_to_f(self, args):
        parms = args.split(",")
        return 'ABCDEF'.find(parms[0][0]) > -1

In get_column_criteria(), you will also pass a list of the JSON keys `['name', 'id']` in your data that you either want to query in a function or that you want passed to your template. 

CriteriaVMCView's logic will apply your functions, using some or all of the JSON keys you pass, to each item in your data to determine if that item should appear in that function's column.

Say the data item being processed is `{'id': 5, 'name': 'Asparagus'}`. The 'args' passed to the a_to_f function will be string `'Asparagus, 5'` since we said our keys were `['name', 'id']`.

The passed string will be split by our function, giving list `['Asparagus', '5']`.

Since our function is only interested in the name, it looks only at `parms[0]` which is 'Asparagus'. And further, since it is only interested in the first letter of name, it only looks at `parms[0][0]` returning True if parms[0][0] is in the range A-F and False if it is not.

In the True case, that item will appear in that column. If False, it will not. Note that items can appear in multiple columns if function criteria overlaps. Conversely an item can appear in no columns if none of the function criteria is met.


.. |evenview| image:: https://user-images.githubusercontent.com/31971607/104204457-4eddfd80-53fb-11eb-9d0d-06db9dafb5c8.gif
    :alt: EvenView
	
.. |criteriaview| image:: https://user-images.githubusercontent.com/31971607/104204473-51d8ee00-53fb-11eb-9824-11f835292ef4.gif
	:alt: CriteriaView
	
.. |definedview| image:: https://user-images.githubusercontent.com/31971607/104204480-53a2b180-53fb-11eb-91f9-98d624ccd170.gif
	:alt: DefinedView