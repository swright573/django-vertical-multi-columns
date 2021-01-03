from django.views.generic import ListView
from vertical_multi_columns.configure import EvenDistribution, CriteriaDistribution, DefinedDistribution

import os
import requests

_api_url = os.environ.get('PLANT_API_URL')
_api_key = {'X-Api-Key': os.environ.get('PLANT_API_KEY')}

def retrieve_data():
    resp = requests.get(_api_url + 'harvesthelper', headers=_api_key)
    raw_api_data = resp.json()
    sorted_api_data = sorted(raw_api_data, key=lambda i: i['name'], reverse=False)
    return sorted_api_data

#This is an example of some returned data in JSON format that has been sorted by name
#sorted_api_data=[{'id': 5, 'name': 'Asparagus'}, {'id': 2, 'name': 'Basil'}, {'id': 6, 'name': 'Beans'},
# {'id': 7, 'name': 'Beets'}, {'id': 24, 'name': 'Bell Peppers'}, # {'id': 8, 'name': 'Broccoli'},
# {'id': 9, 'name': 'Brussels Sprouts'}, {'id': 10, 'name': 'Cabbage'}, {'id': 21, 'name': 'Cantaloupe'},
# {'id': 4, 'name': 'Carrots'}, {'id': 11, 'name': 'Cauliflower'}, {'id': 12, 'name': 'Celery'},
# {'id': 31, 'name': 'Chard'}, {'id': 13, 'name': 'Chives'}, {'id': 38, 'name': 'Cilantro'},
# {'id': 14, 'name': 'Collard Greens'}, {'id': 15, 'name': 'Cucumbers'}, {'id': 45, 'name': 'Dill'},
# {'id': 17, 'name': 'Eggplant'}, {'id': 48, 'name': 'Fred'}, {'id': 49, 'name': 'Fred the Son'},
# {'id': 19, 'name': 'Garlic'}, # {'id': 20, 'name': 'Kale'}, {'id': 3, 'name': 'Lettuce'}, {'id': 40, 'name': 'Mint'},
# {'id': 43, 'name': 'Okra'}, {'id': 18, 'name': 'Onion'}, {'id': 36, 'name': 'Oregano'}, {'id': 39, 'name': 'Parsley'},
# {'id': 22, 'name': 'Parsnips'}, {'id': 23, 'name': 'Peas'}, {'id': 25, 'name': 'Potatoes'},
# {'id': 26, 'name': 'Pumpkins'}, {'id': 27, 'name': 'Radishes'}, {'id': 28, 'name': 'Rhubarb'},
# {'id': 37, 'name': 'Rosemary'}, {'id': 41, 'name': 'Sage'}, {'id': 29, 'name': 'Spinach'},
# {'id': 30, 'name': 'Summer Squash'}, {'id': 16, 'name': 'Sweet Corn'}, {'id': 44, 'name': 'Sweet Potato'},
# {'id': 42, 'name': 'Tarragon'}, {'id': 35, 'name': 'Thyme'}, {'id': 1, 'name': 'Tomatoes'},
# {'id': 32, 'name': 'Turnips'}, {'id': 33, 'name': 'Watermelon'}, {'id': 34, 'name': 'Winter Squash'}]

def simulation_for_DefinedDistribution_example(api_data):

    # This method creates columns that are to be displayed one beside the other using VMC's DefinedDistribution
    def a_to_e(args):
        parms = args.split(",")
        return 'ABCDE'.find(parms[0][0]) > -1

    def f_to_j(args):
        parms = args.split(",")
        return 'FGHIJ'.find(parms[0][0]) > -1

    def k_to_s(args):
        parms = args.split(",")
        return 'KLMNOPQRS'.find(parms[0][0]) > -1

    def t_to_z(args):
        parms = args.split(",")
        return 'TUVWXYZ'.find(parms[0][0]) > -1

    col_funcs = [a_to_e, f_to_j, k_to_s, t_to_z]
    columns = [[] for i in range(len(col_funcs))]
    for i in api_data:
        for j in range(0, len(col_funcs)):
            func = col_funcs[j]
            if func(i['name']):
                columns[j].append(i)
    return columns

class EvenList(ListView):
    # Use VMC's EvenDistribution to evenly divide data into side-by-side columns

    def __init__(self):
        super().__init__()

    def get_queryset(self):
        sorted_api_data = retrieve_data()
        rows = EvenDistribution(sorted_api_data, num_columns=5).process()
        return rows

    template_name = 'evenlist.html'
    context_object_name = "rows"

class CriteriaList(ListView):
    # Use VMC's CriteriaDistribution to divide data into side-by-side columns based on passed functions

    def __init__(self):
        super().__init__()

    # These are examples of functions passed to CriteriaDistribution to handle assignment to columns
    def a_to_f(self, args):
        parms = args.split(",")
        return 'ABCDEFG'.find(parms[0][0]) > -1

    def g_to_s(self, args):
        parms = args.split(",")
        return 'FGHIJKLMNOPQR'.find(parms[0][0]) > -1

    def t_to_z(self, args):
        parms = args.split(",")
        return 'STUVWXYZ'.find(parms[0][0]) > -1
    # down to here

    def get_queryset(self):
        sorted_api_data = retrieve_data()
        column_criteria = [self.a_to_f, self.g_to_s, self.t_to_z]
        rows = CriteriaDistribution(sorted_api_data, column_criteria, ['name', 'id']).process()
        return rows

    template_name = 'criterialist.html'
    context_object_name = "rows"

class DefinedList(ListView):
    # Use VMC's DefinedDistribution to display pre-defined columns side-by-side

    def __init__(self):
        super().__init__()

    def get_queryset(self):
        sorted_api_data = simulation_for_DefinedDistribution_example(retrieve_data())
        rows = DefinedDistribution(sorted_api_data, num_columns=4).process()
        return rows

    template_name = 'definedlist.html'
    context_object_name = "rows"