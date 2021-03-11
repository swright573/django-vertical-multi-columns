************
Example Site
************

There is a example site you can install and run to see the VMC views in action. It has no external requirements other than for you to have pip installed
both Django itself and the django-vertical_multi_columns package.

The example site demonstrates each of the VMC view types in actual use, some using both fairly simple JSON and some using more complex hierarchical JSON.

*Windows commands are shown here. Use the equivalent if you run on Mac or Linux.*

1. Create a directory and change into it. Create a Python virtual directory and activate it using your normal method.

.. code-block:: bash

	mkdir <newdirectory>
	cd newdirectory
	python -m venv <*virtualdirectory*>
	.\<*virtualdirectory*\scripts\activate

2. Install Django and the django-vertical-multi-columns package.

.. code-block:: bash

	pip install django
	pip install django-vertical-multi-columns

3. Copy everything found in the repo under *example_site* to your new directory. Change to subdirectory example_site.

.. code-block:: bash

	xcopy /E <*repo_directory*>\example_site
	cd example_site

4. Change directory up one level and activate the site.

.. code-block:: bash

	cd ..
	python manage.py runserver

5. Point your browser to localhost:8000. More information about the site is provided there under "About the VMC Example Site.
