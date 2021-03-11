"""
Example Site
This site demonstrates how various VMC views are configured.
The same set of data is used in each to demonstrate the different ways data can be displayed.

"""

# import os
# import requests

from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from vertical_multi_columns.views import CriteriaVMCView, DefinedVMCView, EvenVMCView

from . import simulate

# An API call is being simulated here to avoid complexity in this demo program.
# Instead data in JSON format is being returned from simulate.py
# _api_url = os.environ.get('API_URL')
# _api_key = {'X-Api-Key': os.environ.get('API_KEY')}


class About(TemplateView):
    """Verbiage about what the VMC package is all about"""

    #    def get_context_data(self, **kwargs):
    #        """Filler to keep pylint happy"""
    #        pass

    template_name = "about.html"


class EvenVMCSimpleJson(EvenVMCView):
    """Demonstrates the use of EvenVMCView to evenly divide data into side-by-side columns"""

    def __init__(self):
        super().__init__(num_columns=5)

    def get_data(self):
        """Provide the data to be displayed"""
        # resp = requests.get(_api_url, headers=_api_key)
        # raw_api_data = resp.json()
        raw_api_data = simulate.decoded_api_json_data_simple()  # simulation
        sorted_api_data = sorted(raw_api_data, key=lambda i: i["name"], reverse=False)
        return sorted_api_data

    template_name = "evenlistsimplejson.html"
    context_object_name = "rows"


class EvenVMCComplexJson(EvenVMCView):
    """
    Demonstrates the use of EvenVMCView to evenly divide data into side-by-side columns.
    This view makes use of JSON with all data types represented.
    """

    def __init__(self):
        super().__init__(num_columns=2)

    def get_data(self):
        """Provide the data to be displayed"""
        # resp = requests.get(_api_url, headers=_api_key)
        # raw_api_data = resp.json()
        raw_api_data = simulate.decoded_api_json_data_complex()  # simulation
        sorted_api_data = sorted(raw_api_data, key=lambda i: i["string"], reverse=False)
        return sorted_api_data

    template_name = "evenlistcomplexjson.html"
    context_object_name = "rows"


class CriteriaVMCSimpleJson(CriteriaVMCView):
    """
    Demonstrate the use of CriteriaVMCView to assign data to side-by-side columns based on passed functions
    - Look in simulate.py to see the incoming data. There are 4 keys in the JSON string ... "id","name","colour","count".
    """

    # If you want the default number of columns (either set in settings.py or assumed to be 3),
    # you do NOT need to call __init__().
    #
    # def __init__(self):
    #    super().__init__()

    # These are examples of functions you might pass to CriteriaVMCView to handle assignment of data to columns.
    # You can reference any or all of the JSON keys in the data. In this case, "name", "count", and "herb" are used.
    # Data can be any JSON data type.
    def a_to_m_and_count_less_than_10(self, args):
        """Items matching this condition go in column 1"""
        entry_keys = args
        return "ABCDEFGHIJKLM".find(entry_keys[0][0]) > -1 and entry_keys[1] < 10

    def n_to_z_and_count_10_or_greater(self, args):
        """Items matching this condition go in column 2"""
        entry_keys = args
        return "NOPQRSTUVWXYZ".find(entry_keys[0][0]) > -1 and entry_keys[1] >= 10

    def is_herb(self, args):
        """Items matching this condition go in column 3"""
        entry_keys = args
        return entry_keys[2] is True
        # down to here

    def get_data(self):
        """Provide the data to be displayed"""
        # resp = requests.get(_api_url, headers=_api_key)
        # raw_api_data = resp.json()
        raw_api_data = simulate.decoded_api_json_data_simple()  # simulation
        sorted_api_data = sorted(raw_api_data, key=lambda i: i["name"], reverse=False)
        return sorted_api_data

    def get_column_criteria(self):
        """Pass criteria functions and keys"""
        functions = [self.a_to_m_and_count_less_than_10, self.n_to_z_and_count_10_or_greater, self.is_herb]
        keys = ["name", "count", "herb"]
        return functions, keys

    template_name = "criterialistsimplejson.html"
    context_object_name = "rows"


class CriteriaVMCComplexJson(CriteriaVMCView):
    """
    Demonstrate the use of CriteriaVMCView to assign data to side-by-side columns based on passed functions
    - Look in simulate.py to see the incoming data. There are 4 keys in the JSON string ... "id","name","colour","count".
    """

    def __init__(self):
        super().__init__(num_columns=2)

    # These are examples of functions you might pass to CriteriaVMCView for assignment of data to columns.
    # You can reference any or all of the JSON keys in the data.
    # Data can be any JSON data type.
    def boolean_is_true(self, args):
        """Items matching this condition go in column 1"""
        entry_keys = args
        return entry_keys[0]

    def has_111(self, args):
        """Items matching this condition go in column 2"""
        entry_keys = args
        return 111 in entry_keys[1]

    def get_data(self):
        """Provide the data to be displayed"""
        # resp = requests.get(_api_url, headers=_api_key)
        # raw_api_data = resp.json()
        raw_api_data = simulate.decoded_api_json_data_complex()  # simulation
        sorted_api_data = sorted(raw_api_data, key=lambda i: i["string"], reverse=False)
        return sorted_api_data

    def get_column_criteria(self):
        """Pass criteria functions and keys"""
        functions = [self.boolean_is_true, self.has_111]
        keys = ["boolean", "array"]
        return functions, keys

    template_name = "criterialistcomplexjson.html"
    context_object_name = "rows"


class DefinedVMC(DefinedVMCView):
    """Demonstrates the use of DefinedVMCView to display pre-defined columns side-by-side"""

    def __init__(self):
        super().__init__(num_columns=4)

    def get_data(self):
        """Provide the data to be displayed"""
        example_columns = []
        example_columns.append(
            [
                {"id": 8, "name": "Broccoli", "colour": "green", "count": 8, "herb": False},
                {"id": 9, "name": "Brussels Sprouts", "colour": "green", "count": 16, "herb": False},
                {"id": 10, "name": "Cabbage", "colour": "green", "count": 7, "herb": False},
                {"id": 38, "name": "Cilantro", "colour": "green", "count": 8, "herb": True},
                {"id": 14, "name": "Collard Greens", "colour": "green", "count": 14, "herb": False},
                {"id": 15, "name": "Cucumbers", "colour": "green", "count": 9, "herb": False},
                {"id": 45, "name": "Dill", "colour": "green", "count": 4, "herb": True},
                {"id": 17, "name": "Eggplant", "colour": "purple", "count": 8, "herb": False},
                {"id": 22, "name": "Parsnips", "colour": "white", "count": 8, "herb": False},
                {"id": 23, "name": "Peas", "colour": "green", "count": 4, "herb": False},
                {"id": 25, "name": "Potatoes", "colour": "white", "count": 8, "herb": False},
                {"id": 26, "name": "Pumpkins", "colour": "orange", "count": 8, "herb": False},
                {"id": 27, "name": "Radishes", "colour": "red", "count": 8, "herb": False},
            ]
        )
        example_columns.append(
            [
                {"id": 5, "name": "Asparagus", "colour": "green", "count": 9, "herb": False},
                {"id": 2, "name": "Basil", "colour": "green", "count": 5, "herb": True},
                {"id": 3, "name": "Lettuce", "colour": "green", "count": 7, "herb": False},
                {"id": 40, "name": "Mint", "colour": "green", "count": 4, "herb": True},
                {"id": 43, "name": "Okra", "colour": "green", "count": 4, "herb": False},
                {"id": 37, "name": "Rosemary", "colour": "green", "count": 8, "herb": True},
                {"id": 41, "name": "Sage", "colour": "green", "count": 4, "herb": True},
                {"id": 29, "name": "Spinach", "colour": "green", "count": 7, "herb": False},
                {"id": 30, "name": "Summer Squash", "colour": "yellow", "count": 12, "herb": False},
                {"id": 16, "name": "Sweet Corn", "colour": "yellow", "count": 10, "herb": False},
            ]
        )
        example_columns.append(
            [
                {"id": 11, "name": "Cauliflower", "colour": "white", "count": 11, "herb": False},
                {"id": 12, "name": "Celery", "colour": "green", "count": 6, "herb": False},
                {"id": 31, "name": "Chard", "colour": "green", "count": 5, "herb": False},
                {"id": 36, "name": "Oregano", "colour": "green", "count": 7, "herb": True},
                {"id": 39, "name": "Parsley", "colour": "green", "count": 7, "herb": True},
                {"id": 1, "name": "Tomatoes", "colour": "red", "count": 8, "herb": False},
                {"id": 32, "name": "Turnips", "colour": "white", "count": 7, "herb": False},
                {"id": 33, "name": "Watermelon", "colour": "red", "count": 10, "herb": False},
                {"id": 34, "name": "Winter Squash", "colour": "orange", "count": 13, "herb": False},
            ]
        )
        example_columns.append(
            [
                {"id": 6, "name": "Beans", "colour": "yellow", "count": 5, "herb": False},
                {"id": 7, "name": "Beets", "colour": "red", "count": 5, "herb": False},
                {"id": 24, "name": "Bell Peppers", "colour": "red", "count": 12, "herb": False},
                {"id": 21, "name": "Cantaloupe", "colour": "orange", "count": 10, "herb": False},
                {"id": 4, "name": "Carrots", "colour": "orange", "count": 7, "herb": False},
                {"id": 13, "name": "Chives", "colour": "green", "count": 6, "herb": True},
                {"id": 19, "name": "Garlic", "colour": "white", "count": 6, "herb": True},
                {"id": 20, "name": "Kale", "colour": "green", "count": 4, "herb": False},
                {"id": 18, "name": "Onion", "colour": "white", "count": 5, "herb": False},
                {"id": 28, "name": "Rhubarb", "colour": "red", "count": 7, "herb": False},
                {"id": 44, "name": "Sweet Potato", "colour": "orange", "count": 12, "herb": False},
                {"id": 42, "name": "Tarragon", "colour": "green", "count": 8, "herb": True},
                {"id": 35, "name": "Thyme", "colour": "green", "count": 5, "herb": True},
            ]
        )
        return example_columns

    template_name = "definedlist.html"
    context_object_name = "rows"


class StandardDjango(ListView):
    """A standard Django ListView display"""

    def get(self, request):
        """Provide the data to be displayed"""
        raw_api_data = simulate.decoded_api_json_data_simple()  # simulation
        sorted_api_data = sorted(raw_api_data, key=lambda i: i["name"], reverse=False)
        return render(request, "standard_django.html", {"rows": sorted_api_data})
