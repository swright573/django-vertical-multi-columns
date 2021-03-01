************
Example Site
************

There is a example site you can install and run to see the VMC views in action. It has no external requirements other than for you to have pip installed
both Django itself and the django-vertical_multi_columns package.

The example site demonstrates each of the VMC view types in actual use, some using both simpler and more complex JSON data types.

(*Windows commands are shown. Use the equivalent if you run on Mac or Linux.*)

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

6. Activate the site.

.. code-block:: bash

	python manage.py runserver

7. Point your browser to localhost:8000. More information about the site is provided there under "About the VMC Example Site.
