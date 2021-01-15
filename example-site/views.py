from django.views.generic import TemplateView
from vertical_multi_columns.views import EvenVMCView, CriteriaVMCView, DefinedVMCView
#import os
#import requests
from . import simulate

# An API call is being simulated here to avoid complexity in this demo program.
# Instead data in JSON format is being returned from simulate.py

#_api_url = os.environ.get('API_URL')
#_api_key = {'X-Api-Key': os.environ.get('API_KEY')}

class Home(TemplateView):

    def __init__(self, **kwargs):
        super().__init__()

    template_name = 'home.html'


class EvenVMC(EvenVMCView):
    # Use VMC's Even distribution to evenly divide data into side-by-side columns

    def __init__(self, **kwargs):
        super().__init__(num_columns=5)

    def get_data(self):
#       resp = requests.get(_api_url, headers=_api_key)
#       raw_api_data = resp.json()
        raw_api_data = simulate.api_data_json()   # simulation
        sorted_api_data = sorted(raw_api_data, key=lambda i: i['name'], reverse=False)
        return sorted_api_data

    template_name = 'evenlist.html'
    context_object_name = "rows"

class CriteriaVMC(CriteriaVMCView):
    # Use VMC's Criteria distribution to divide data into side-by-side columns based on passed functions

    def __init__(self, **kwargs):
        super().__init__(num_columns=3)

    # These are examples of functions you can pass to CriteriaVMCView to handle assignment to columns
    def a_to_f(self, args):
        parms = args.split(",")
        return 'ABCDEF'.find(parms[0][0]) > -1

    def g_to_s(self, args):
        parms = args.split(",")
        return 'GHIJKLMNOPQRS'.find(parms[0][0]) > -1

    def t_to_z(self, args):
        parms = args.split(",")
        return 'TUVWXYZ'.find(parms[0][0]) > -1
    # down to here

    def get_data(self):
        #resp = requests.get(_api_url, headers=_api_key)
        #raw_api_data = resp.json()
        raw_api_data = simulate.api_data_json()  # simulation
        sorted_api_data = sorted(raw_api_data, key=lambda i: i['name'], reverse=False)
        return sorted_api_data

    def get_column_criteria(self):
        functions = [self.a_to_f, self.g_to_s, self.t_to_z]
        keys = ['name', 'id']
        return functions, keys

    template_name = 'criterialist.html'
    context_object_name = "rows"

class DefinedVMC(DefinedVMCView):
    # Use VMC's DefinedDistribution to display pre-defined columns side-by-side

    def __init__(self, **kwargs):
        super().__init__(num_columns=4)

    def get_data(self):
        example_columns = []
        example_columns.append([{'id': 5, 'name': 'Asparagus'}, {'id': 2, 'name': 'Basil'}, {'id': 6, 'name': 'Beans'},
                                {'id': 7, 'name': 'Beets'}, {'id': 24, 'name': 'Bell Peppers'},
                                {'id': 8, 'name': 'Broccoli'}, {'id': 9, 'name': 'Brussels Sprouts'},
                                {'id': 10, 'name': 'Cabbage'}, {'id': 21, 'name': 'Cantaloupe'}])
        example_columns.append([{'id': 19, 'name': 'Garlic'}])
        example_columns.append([{'id': 20, 'name': 'Kale'}, {'id': 3, 'name': 'Lettuce'}, {'id': 40, 'name': 'Mint'},
                                {'id': 43, 'name': 'Okra'}, {'id': 18, 'name': 'Onion'}, {'id': 36, 'name': 'Oregano'},
                                {'id': 39, 'name': 'Parsley'}])
        example_columns.append(
            [{'id': 42, 'name': 'Tarragon'}, {'id': 35, 'name': 'Thyme'}, {'id': 1, 'name': 'Tomatoes'},
             {'id': 32, 'name': 'Turnips'}, {'id': 33, 'name': 'Watermelon'},
             {'id': 34, 'name': 'Winter Squash'}])
        return example_columns

    template_name = 'definedlist.html'
    context_object_name = "rows"