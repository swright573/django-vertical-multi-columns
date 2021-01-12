=====
Usage
=====

There are 3 VMC views available. These views are all subclasses of Django's ListView so all its capabilities are still available to you in addition to the specific VMC capabilities described below.

Available Views
---------------

**EvenVMCView** Spreads your data across the number of columns you specify, keeping the length of the columns as even as possible.

|evenview|

**CriteriaVMCView** You provide a list of functions, one per column, that VMC uses to determine which column an item will be placed in.

|criteriaview|

**DefinedVMCView** You already have the columns you want displayed. You provide a column list and VMC does the rest.
 
|definedview|


EvenVMCView
define method get_data() to retrieve a list of data to be displayed which must be in JSON format.
	
CriteriaVMCView
define method get_data() to retrieve a list of data to be displayed which must be in JSON format.
define method get_column_criteria() to define logic used to place data items into columns
	 
DefinedVMCView
define method get_data() to retrieve a list of pre-defined columns which must be in JSON format.

Sample Code
-----------

This example implements EvenVMCView but they are all fairly similar. Differences are noted below. Note that the example is pulling API data via requests but data from any source can be used.

.. code-block:: python

    from vertical_multi_columns.configure import EvenVMCView
	import requests


.. code-block:: python

	class MyEvenView(EvenVMCView):
		def __init__(self, **kwargs):
			# You can pass an optional num_columns kwarg to override the value in settings.
			# If there is nothing in settings and you don't pass num_columns, the number of columns will be 3.
			super().__init__(num_columns=5)

		def get_data(self):
			# Write logic to retrieve the data to be displayed (often from an API) and return it sorted in the desired order.
			# Data must be in JSON format.
			resp = requests.get(<api_url>)
			raw_api_data = resp.json()
			sorted_api_data = sorted(raw_api_data, key=lambda i: i['<field>'])
			return sorted_api_data

		template_name = '<your_template>.html'
		context_object_name = "<your_choice>"

Sample App
----------
There is a sample app ...



.. |evenview| image:: https://user-images.githubusercontent.com/31971607/104204457-4eddfd80-53fb-11eb-9d0d-06db9dafb5c8.gif
    :alt: EvenView
	
.. |criteriaview| image:: https://user-images.githubusercontent.com/31971607/104204473-51d8ee00-53fb-11eb-9824-11f835292ef4.gif
	:alt: CriteriaView
	
.. |definedview| image:: https://user-images.githubusercontent.com/31971607/104204480-53a2b180-53fb-11eb-91f9-98d624ccd170.gif
	:alt: DefinedView