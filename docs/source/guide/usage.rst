*****
Usage
*****

There are 3 VMC views available. They are all subclasses of Django's ListView so in addition to the specific VMC capabilities described below, all ListView's capabilities are still available to you.

View Options
------------

**EvenVMCView** 

Spreads your data across the number of columns you specify, keeping the length of the columns as even as possible.

|evenview|

**CriteriaVMCView** 

You provide a list of functions, one per column, that VMC uses to determine which column an item will be placed in.

|criteriaview|

**DefinedVMCView** 

You already have the columns you want displayed. You provide a column list and VMC does the rest.
 
|definedview|

Required Method Overrides
-------------------------

Some methods in the VMC classes must be overridden.

**EvenVMCView**

In your view, define a method ``get_data()`` to return a list of data to be displayed, sorted as you wish, and returned in JSON format.
	
**CriteriaVMCView**

In your view, define 2 methods:

* ``get_data()`` to return a list of data, sorted as you wish. It must be in JSON format.
* ``get_column_criteria()`` to retrieve two things ...
	1. a list of functions to be used to place data items into columns, one function for each column.
	2. a list of the dictionary keys referenced in the functions.
	 
**DefinedVMCView**

In your view, define a method ``get_data()`` to return a list of pre-defined columns in JSON format.

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

.. code:block:: bash
	
	python -m venv <*virtualdirectory*>
	.\<*virtualdirectory*\scripts\activate

2. Install Django and the django-vertical-multi-columns package.

.. code-block:: bash

	pip install django
	pip install django-vertical-multi-columns

3. Create a new Django project called vmcexamplesite.

.. code-block:: bash

	django-admin startproject vmcexamplesite
	
4. Copy all the files in example-site in the repo into the vmcexamplesite directory Django just created.

.. code-block:: bash
	
	cd .\vmcexamplesite
	copy <*repodirectory*>\example-site\*.*
	
5. Update settings.py with your secret key (*or use an environment variable*)

.. code-block:: bash

	...
	SECRET_KEY = <*insert your Django secret key here*>
	...

6. Execute runserver to activate the site.

.. code-block:: bash

	python manage.py runserver
	
7. Point your browser to localhost:8000. More information about the site is provided there under "About the VMC Example Site.


.. |evenview| image:: https://user-images.githubusercontent.com/31971607/104204457-4eddfd80-53fb-11eb-9d0d-06db9dafb5c8.gif
    :alt: EvenView
	
.. |criteriaview| image:: https://user-images.githubusercontent.com/31971607/104204473-51d8ee00-53fb-11eb-9824-11f835292ef4.gif
	:alt: CriteriaView
	
.. |definedview| image:: https://user-images.githubusercontent.com/31971607/104204480-53a2b180-53fb-11eb-91f9-98d624ccd170.gif
	:alt: DefinedView