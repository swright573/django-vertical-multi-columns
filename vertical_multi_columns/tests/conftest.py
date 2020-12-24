import pytest
import random
from django.conf import settings

@pytest.fixture()
def settings_NUMBER_OF_COLUMNS_Null():
    settings.VERTICAL_MULTI_COLUMNS = {}

@pytest.fixture()
def settings_NUMBER_OF_COLUMNS_3():
    settings.VERTICAL_MULTI_COLUMNS = {'NUMBER_OF_COLUMNS': 3}

@pytest.fixture()
def settings_NUMBER_OF_COLUMNS_4():
    settings.VERTICAL_MULTI_COLUMNS = {'NUMBER_OF_COLUMNS': 4}

@pytest.fixture()
def settings_NUMBER_OF_COLUMNS_5():
    settings.VERTICAL_MULTI_COLUMNS = {'NUMBER_OF_COLUMNS': 5}

@pytest.fixture()
def entries_27():
    # This list has 27 entries
    return \
        [{'id':5,'name':'Asparagus'},{'id':6,'name':'Beans'},{'id':7,'name':'Beets'},
         {'id':24,'name':'Bell Peppers'},{'id':8,'name':'Broccoli'},{'id':9,'name':'Brussels Sprouts'},
         {'id':10,'name':'Cabbage'},{'id':4,'name':'Carrots'},{'id':11,'name':'Cauliflower'},
         {'id':12,'name':'Celery'},{'id':31,'name':'Chard'},{'id':14,'name':'Collard Greens'},
         {'id':15,'name':'Cucumbers'},{'id':17,'name':'Eggplant'},{'id':19,'name':'Garlic'},
         {'id':20,'name':'Kale'},{'id':3,'name':'Lettuce'},{'id':18,'name':'Onion'},
         {'id':22,'name':'Parsnips'},{'id':23,'name':'Peas'},{'id':25,'name':'Potatoes'},
         {'id':27,'name':'Radishes'},{'id':29,'name':'Spinach'},{'id':16,'name':'Sweet Corn'},
         {'id':44,'name':'Sweet Potato'},{'id':1,'name':'Tomatoes'},{'id':32,'name':'Turnips'}]

@pytest.fixture()
def entries_4():
    # This list has 4 entries
    return [{'id':5,'name':'Asparagus'},
            {'id':20,'name':'Kale'},
            {'id':44,'name':'Sweet Potato'},
            {'id':34,'name':'Winter Squash'}]

@pytest.fixture()
def entries_0():
    # This list has 0 entries
    return []

@pytest.fixture()
def padded_columns_16():
    return [[{'id': 5, 'name': 'Asparagus'}, {'id': 2, 'name': 'Basil'}, {'id': 6, 'name': 'Beans'}, {'id': 7, 'name': 'Beets'}, {'id': 24, 'name': 'Bell Peppers'}, {'id': 8, 'name': 'Broccoli'}, {'id': 9, 'name': 'Brussels Sprouts'}, {'id': 10, 'name': 'Cabbage'}, {'id': 21, 'name': 'Cantaloupe'}, {'id': 4, 'name': 'Carrots'}, {'id': 11, 'name': 'Cauliflower'}, {'id': 12, 'name': 'Celery'}, {'id': 31, 'name': 'Chard'}, {'id': 13, 'name': 'Chives'}, {'id': 38, 'name': 'Cilantro'}, {'id': 14, 'name': 'Collard Greens'}], 
            [{'id': 15, 'name': 'Cucumbers'}, {'id': 45, 'name': 'Dill'}, {'id': 17, 'name': 'Eggplant'}, {'id': 48, 'name': 'Fred'}, {'id': 49, 'name': 'Fred the Son'}, {'id': 19, 'name': 'Garlic'}, {'id': 20, 'name': 'Kale'}, {'id': 3, 'name': 'Lettuce'}, {'id': 40, 'name': 'Mint'}, {'id': 43, 'name': 'Okra'}, {'id': 18, 'name': 'Onion'}, {'id': 36, 'name': 'Oregano'}, {'id': 39, 'name': 'Parsley'}, {'id': 22, 'name': 'Parsnips'}, {'id': 23, 'name': 'Peas'}, {'id': 25, 'name': 'Potatoes'}], 
            [{'id': 26, 'name': 'Pumpkins'}, {'id': 27, 'name': 'Radishes'}, {'id': 28, 'name': 'Rhubarb'}, {'id': 37, 'name': 'Rosemary'}, {'id': 41, 'name': 'Sage'}, {'id': 29, 'name': 'Spinach'}, {'id': 30, 'name': 'Summer Squash'}, {'id': 16, 'name': 'Sweet Corn'}, {'id': 44, 'name': 'Sweet Potato'}, {'id': 42, 'name': 'Tarragon'}, {'id': 35, 'name': 'Thyme'}, {'id': 1, 'name': 'Tomatoes'}, {'id': 32, 'name': 'Turnips'}, {'id': 33, 'name': 'Watermelon'}, {'id': 34, 'name': 'Winter Squash'}, '']]

@pytest.fixture()
def padded_columns_4():
    return [[{'id': 5, 'name': 'Asparagus'}, {'id': 2, 'name': 'Basil'}, {'id': 6, 'name': 'Beans'}, {'id': 7, 'name': 'Beets'}],
            [{'id': 15, 'name': 'Cucumbers'}, {'id': 45, 'name': 'Dill'}, {'id': 17, 'name': 'Eggplant'}, {'id': 48, 'name': 'Fred'}],
            [{'id': 26, 'name': 'Pumpkins'}, {'id': 27, 'name': 'Radishes'}, {'id': 28, 'name': 'Rhubarb'}, '']]

@pytest.fixture()
def columns_many():
    def _build_cols(num_items, num_cols):
        col = [{} for i in range(num_items-random.randint(0,num_items))]
        cols = [col for i in range(num_cols)]
        # adding one more line to ensure there is at least one line with the full num_items in it
        cols.append([{} for i in range(num_items)])
        return cols
    return _build_cols

@pytest.fixture()
def columns_same_length_4():
    return [[{'id':5,'name':'Asparagus'},{'id':2,'name':'Basil'},{'id':6,'name':'Beans'},{'id':7,'name':'Beets'}],
            [{'id':15,'name':'Cucumbers'},{'id':45,'name':'Dill'},{'id':17,'name':'Eggplant'},{'id':19,'name':'Garlic'}],
            [{'id':26,'name':'Pumpkins'},{'id':27,'name':'Radishes'},{'id':28,'name':'Rhubarb'},{'id':29,'name':'Spinach'}]]

@pytest.fixture()
def first_column_empty_5():
    return [[],
            [{'id':15,'name':'Cucumbers'},{'id':45,'name':'Dill'},{'id':17,'name':'Eggplant'},{'id':19,'name':'Garlic'},{'id':3,'name':'Lettuce'}],
            [{'id':26,'name':'Pumpkins'},{'id':27,'name':'Radishes'},{'id':28,'name':'Rhubarb'},{'id':29,'name':'Spinach'},{'id':16,'name':'Sweet Corn'}]]

@pytest.fixture()
def last_column_empty_2():
    return [[{'id':5,'name':'Asparagus'},{'id':2,'name':'Basil'}],
            [{'id':15,'name':'Cucumbers'},{'id':45,'name':'Dill'}],
            [{'id':22,'name':'Parsnips'},{'id':23,'name':'Peas'}],
            []]

@pytest.fixture()
def all_columns_empty():
    return [[] for i in range(0, 100)]

@pytest.fixture()
def criteria_functions_2():
    def a_to_m(args):
            parms = args.split(",")
            return 'ABCDEFGHIJKLM'.find(parms[0][0]) > -1
    def n_to_z(args):
        parms = args.split(",")
        return 'NOPQRSTUVWXYZ'.find(parms[0][0]) > -1
    return [a_to_m, n_to_z]

@pytest.fixture()
def criteria_functions_3():
    def a_to_f(args):
            parms = args.split(",")
            return 'ABCDEF'.find(parms[0][0]) > -1
    def g_to_s(args):
        parms = args.split(",")
        return 'GHIJKLMNOPQRS'.find(parms[0][0]) > -1
    def t_to_z(args):
        parms = args.split(",")
        return 'TUVWXYZ'.find(parms[0][0]) > -1
    return [a_to_f, g_to_s, t_to_z]

@pytest.fixture()
def criteria_functions_4():
    def a_to_d(args):
            parms = args.split(",")
            return 'ABCD'.find(parms[0][0]) > -1
    def e_to_m(args):
        parms = args.split(",")
        return 'EFGHIJKLM'.find(parms[0][0]) > -1
    def n_to_r(args):
        parms = args.split(",")
        return 'NOPQR'.find(parms[0][0]) > -1
    def s_to_z(args):
        parms = args.split(",")
        return 'STUVWXYZ'.find(parms[0][0]) > -1
    return [a_to_d, e_to_m, n_to_r, s_to_z]

@pytest.fixture()
def function_args():
    return ['name', 'id']
