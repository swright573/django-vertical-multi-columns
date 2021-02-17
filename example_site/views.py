"""
Example Site
This site demonstrates how various VMC views are configured.
The same set of data is used in each to demonstrate the different ways data can be displayed.

"""

# import os
# import requests

from django.shortcuts import render
from django.views.generic import ListView, View

from vertical_multi_columns.views import CriteriaVMCView, DefinedVMCView, EvenVMCView

from . import simulate

# An API call is being simulated here to avoid complexity in this demo program.
# Instead data in JSON format is being returned from simulate.py
# _api_url = os.environ.get('API_URL')
# _api_key = {'X-Api-Key': os.environ.get('API_KEY')}


class About(View):
    """Verbiage about what the VMC package is all about"""

    #    def get_context_data(self, **kwargs):
    #        """Filler to keep pylint happy"""
    #        pass

    template_name = "about.html"


class EvenVMC(EvenVMCView):
    """Demonstrates the use of EvenVMCView to evenly divide data into side-by-side columns"""

    def __init__(self):
        super().__init__(num_columns=5)

    def get_data(self):
        """Provide the data to be displayed"""
        # resp = requests.get(_api_url, headers=_api_key)
        # raw_api_data = resp.json()
        raw_api_data = simulate.api_data_json()  # simulation
        sorted_api_data = sorted(raw_api_data, key=lambda i: i["name"], reverse=False)
        return sorted_api_data

    template_name = "evenlist.html"
    context_object_name = "rows"


class CriteriaVMC(CriteriaVMCView):
    """Demonstrate the use of CriteriaVMCView to assign data to side-by-side columns based on passed functions"""

    # def __init__(self):
    #    super().__init__()

    # These are examples of functions you can might pass to CriteriaVMCView to handle assignment to columns
    def a_to_f(self, args):
        """Identify items starting with the letters A - F"""
        parms = args.split(",")
        return "ABCDEF".find(parms[0][0]) > -1

    def g_to_s(self, args):
        """Identify items starting with the letters G - S"""
        parms = args.split(",")
        return "GHIJKLMNOPQRS".find(parms[0][0]) > -1

    def t_to_z(self, args):
        """Identify items starting with the letters T - Z"""
        parms = args.split(",")
        return "TUVWXYZ".find(parms[0][0]) > -1

    # down to here

    def get_data(self):
        """Provide the data to be displayed"""
        # resp = requests.get(_api_url, headers=_api_key)
        # raw_api_data = resp.json()
        raw_api_data = simulate.api_data_json()  # simulation
        sorted_api_data = sorted(raw_api_data, key=lambda i: i["name"], reverse=False)
        return sorted_api_data

    def get_column_criteria(self):
        """Pass criteria functions and keys"""
        functions = [self.a_to_f, self.g_to_s, self.t_to_z]
        keys = ["name", "id"]
        return functions, keys

    template_name = "criterialist.html"
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
                {"id": 5, "name": "Asparagus"},
                {"id": 2, "name": "Basil"},
                {"id": 6, "name": "Beans"},
                {"id": 31, "name": "Chard"},
                {"id": 13, "name": "Chives"},
                {"id": 38, "name": "Cilantro"},
                {"id": 18, "name": "Onion"},
                {"id": 36, "name": "Oregano"},
                {"id": 39, "name": "Parsley"},
                {"id": 33, "name": "Watermelon"},
                {"id": 34, "name": "Winter Squash"},
            ]
        )
        example_columns.append(
            [
                {"id": 4, "name": "Carrots"},
                {"id": 11, "name": "Cauliflower"},
                {"id": 12, "name": "Celery"},
                {"id": 3, "name": "Lettuce"},
                {"id": 40, "name": "Mint"},
                {"id": 43, "name": "Okra"},
                {"id": 37, "name": "Rosemary"},
                {"id": 41, "name": "Sage"},
                {"id": 29, "name": "Spinach"},
            ]
        )
        example_columns.append(
            [
                {"id": 7, "name": "Beets"},
                {"id": 24, "name": "Bell Peppers"},
                {"id": 8, "name": "Broccoli"},
                {"id": 22, "name": "Parsnips"},
                {"id": 23, "name": "Peas"},
                {"id": 25, "name": "Potatoes"},
                {"id": 32, "name": "Turnips"},
            ]
        )
        example_columns.append(
            [
                {"id": 9, "name": "Brussels Sprouts"},
                {"id": 10, "name": "Cabbage"},
                {"id": 21, "name": "Cantaloupe"},
                {"id": 14, "name": "Collard Greens"},
                {"id": 15, "name": "Cucumbers"},
                {"id": 45, "name": "Dill"},
                {"id": 17, "name": "Eggplant"},
                {"id": 19, "name": "Garlic"},
                {"id": 20, "name": "Kale"},
                {"id": 26, "name": "Pumpkins"},
                {"id": 27, "name": "Radishes"},
                {"id": 28, "name": "Rhubarb"},
                {"id": 30, "name": "Summer Squash"},
                {"id": 16, "name": "Sweet Corn"},
                {"id": 44, "name": "Sweet Potato"},
                {"id": 42, "name": "Tarragon"},
                {"id": 35, "name": "Thyme"},
                {"id": 1, "name": "Tomatoes"},
            ]
        )
        return example_columns

    template_name = "definedlist.html"
    context_object_name = "rows"


class StandardDjango(ListView):
    """A standard Django ListView display"""

    def get(self, request):
        """Provide the data to be displayed"""
        raw_api_data = simulate.api_data_json()  # simulation
        sorted_api_data = sorted(raw_api_data, key=lambda i: i["name"], reverse=False)
        return render(request, "standard_django.html", {"rows": sorted_api_data})
