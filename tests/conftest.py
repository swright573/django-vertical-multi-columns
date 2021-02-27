"""
Common elements for pytest tests

"""

import random

import pytest
from django.conf import settings


def pytest_configure():
    """Initialize Django settings"""
    settings.configure(
        INSTALLED_APPS=[
            "vertical_multi_columns",
        ]
    )


# Fixtures for setting NUMBER_OF_COLUMNS
@pytest.fixture()
def settings_number_of_columns_null():
    """There is no setting for NUMBER_OF_COLUMNS"""
    settings.VERTICAL_MULTI_COLUMNS = None


@pytest.fixture()
def settings_number_of_columns_2():
    """Django setting for NUMBER_OF_COLUMNS is 2"""
    settings.VERTICAL_MULTI_COLUMNS = [{"NUMBER_OF_COLUMNS": 2}]


@pytest.fixture()
def settings_number_of_columns_3():
    """Django setting for NUMBER_OF_COLUMNS is 3"""
    settings.VERTICAL_MULTI_COLUMNS = [{"NUMBER_OF_COLUMNS": 3}]


@pytest.fixture()
def settings_number_of_columns_4():
    """Django setting for NUMBER_OF_COLUMNS is 4"""
    settings.VERTICAL_MULTI_COLUMNS = [{"NUMBER_OF_COLUMNS": 4}]


@pytest.fixture()
def settings_number_of_columns_5():
    """Django setting for NUMBER_OF_COLUMNS is 5"""
    settings.VERTICAL_MULTI_COLUMNS = [{"NUMBER_OF_COLUMNS": 5}]


# Fixtures for representing data input to a VMC view
@pytest.fixture()
def entries_27():
    """Input data with 27 entries"""
    return [
        {"id": 5, "name": "Asparagus", "colour": "green", "count": 9, "herb": False},
        {"id": 2, "name": "Basil", "colour": "green", "count": 5, "herb": True},
        {"id": 6, "name": "Beans", "colour": "yellow", "count": 5, "herb": False},
        {"id": 8, "name": "Broccoli", "colour": "green", "count": 8, "herb": False},
        {"id": 9, "name": "Brussels Sprouts", "colour": "green", "count": 16, "herb": False},
        {"id": 10, "name": "Cabbage", "colour": "green", "count": 7, "herb": False},
        {"id": 21, "name": "Cantaloupe", "colour": "orange", "count": 10, "herb": False},
        {"id": 11, "name": "Cauliflower", "colour": "white", "count": 11, "herb": False},
        {"id": 12, "name": "Celery", "colour": "green", "count": 6, "herb": False},
        {"id": 13, "name": "Chives", "colour": "green", "count": 6, "herb": True},
        {"id": 38, "name": "Cilantro", "colour": "green", "count": 8, "herb": True},
        {"id": 14, "name": "Collard Greens", "colour": "green", "count": 14, "herb": False},
        {"id": 45, "name": "Dill", "colour": "green", "count": 4, "herb": True},
        {"id": 36, "name": "Oregano", "colour": "green", "count": 7, "herb": True},
        {"id": 39, "name": "Parsley", "colour": "green", "count": 7, "herb": True},
        {"id": 22, "name": "Parsnips", "colour": "white", "count": 8, "herb": False},
        {"id": 23, "name": "Peas", "colour": "green", "count": 4, "herb": False},
        {"id": 25, "name": "Potatoes", "colour": "white", "count": 8, "herb": False},
        {"id": 26, "name": "Pumpkins", "colour": "orange", "count": 8, "herb": False},
        {"id": 37, "name": "Rosemary", "colour": "green", "count": 8, "herb": True},
        {"id": 41, "name": "Sage", "colour": "green", "count": 4, "herb": True},
        {"id": 29, "name": "Spinach", "colour": "green", "count": 7, "herb": False},
        {"id": 30, "name": "Summer Squash", "colour": "yellow", "count": 12, "herb": False},
        {"id": 16, "name": "Sweet Corn", "colour": "yellow", "count": 10, "herb": False},
        {"id": 33, "name": "Watermelon", "colour": "red", "count": 10, "herb": False},
        {"id": 34, "name": "Winter Squash", "colour": "orange", "count": 13, "herb": False},
    ]


@pytest.fixture()
def entries_4():
    """Input data with 4 entries"""
    return [
        {"id": 5, "name": "Asparagus", "colour": "green", "count": 9, "herb": False},
        {"id": 20, "name": "Kale", "colour": "green", "count": 4, "herb": False},
        {"id": 44, "name": "Sweet Potato", "colour": "orange", "count": 12, "herb": False},
        {"id": 34, "name": "Winter Squash", "colour": "orange", "count": 13, "herb": False},
    ]


@pytest.fixture()
def entries_0():
    """Empty input data"""
    return []


# Fixtures for representing data out
@pytest.fixture()
def columns_4():
    """4 columns of out data, each having a varying number of entries"""
    return [
        [
            {"id": 5, "name": "Asparagus", "colour": "green", "count": 9, "herb": False},
            {"id": 2, "name": "Basil", "colour": "green", "count": 5, "herb": True},
            {"id": 6, "name": "Beans", "colour": "yellow", "count": 5, "herb": False},
            {"id": 8, "name": "Broccoli", "colour": "green", "count": 8, "herb": False},
        ],
        [{"id": 48, "name": "Fred"}, {"id": 19, "name": "Garlic"}],
        [
            {"id": 26, "name": "Pumpkins", "colour": "orange", "count": 8, "herb": False},
            {"id": 37, "name": "Rosemary", "colour": "green", "count": 8, "herb": True},
            {"id": 41, "name": "Sage", "colour": "green", "count": 4, "herb": True},
            {"id": 29, "name": "Spinach", "colour": "green", "count": 7, "herb": False},
            {"id": 30, "name": "Summer Squash", "colour": "yellow", "count": 12, "herb": False},
        ],
        [
            {"id": 16, "name": "Sweet Corn", "colour": "yellow", "count": 10, "herb": False},
            {"id": 33, "name": "Watermelon", "colour": "red", "count": 10, "herb": False},
            {"id": 34, "name": "Winter Squash", "colour": "orange", "count": 13, "herb": False},
        ],
    ]


@pytest.fixture()
def columns_2():
    """2 columns of out data, each having a varying number of entries"""
    return [
        [
            {"id": 5, "name": "Asparagus", "colour": "green", "count": 9, "herb": False},
            {"id": 2, "name": "Basil", "colour": "green", "count": 5, "herb": True},
            {"id": 6, "name": "Beans", "colour": "yellow", "count": 5, "herb": False},
            {"id": 8, "name": "Broccoli", "colour": "green", "count": 8, "herb": False},
            {"id": 9, "name": "Brussels Sprouts", "colour": "green", "count": 16, "herb": False},
            {"id": 10, "name": "Cabbage", "colour": "green", "count": 7, "herb": False},
        ],
        [
            {"id": 41, "name": "Sage", "colour": "green", "count": 4, "herb": True},
            {"id": 29, "name": "Spinach", "colour": "green", "count": 7, "herb": False},
            {"id": 30, "name": "Summer Squash", "colour": "yellow", "count": 12, "herb": False},
        ],
    ]


def padded_columns_16():
    """
    Columns with 16 entries where some entries are blank to fill shorter columns to match the longest
    Used in parametrized fixture "padded_columns"
    """
    return [
        [
            {"id": 5, "name": "Asparagus", "colour": "green", "count": 9, "herb": False},
            {"id": 2, "name": "Basil", "colour": "green", "count": 5, "herb": True},
            {"id": 6, "name": "Beans", "colour": "yellow", "count": 5, "herb": False},
            {"id": 7, "name": "Beets", "colour": "red", "count": 5, "herb": False},
            {"id": 24, "name": "Bell Peppers", "colour": "red", "count": 12, "herb": False},
            {"id": 8, "name": "Broccoli", "colour": "green", "count": 8, "herb": False},
            {"id": 9, "name": "Brussels Sprouts", "colour": "green", "count": 16, "herb": False},
            {"id": 10, "name": "Cabbage", "colour": "green", "count": 7, "herb": False},
            {"id": 21, "name": "Cantaloupe", "colour": "orange", "count": 10, "herb": False},
            {"id": 4, "name": "Carrots", "colour": "orange", "count": 7, "herb": False},
            {"id": 11, "name": "Cauliflower", "colour": "white", "count": 11, "herb": False},
            {"id": 12, "name": "Celery", "colour": "green", "count": 6, "herb": False},
            {"id": 31, "name": "Chard", "colour": "green", "count": 5, "herb": False},
            {"id": 13, "name": "Chives", "colour": "green", "count": 6, "herb": True},
            {"id": 38, "name": "Cilantro", "colour": "green", "count": 8, "herb": True},
            {"id": 14, "name": "Collard Greens", "colour": "green", "count": 14, "herb": False},
        ],
        [
            {"id": 15, "name": "Cucumbers", "colour": "green", "count": 9, "herb": False},
            {"id": 45, "name": "Dill", "colour": "green", "count": 4, "herb": True},
            {"id": 17, "name": "Eggplant", "colour": "purple", "count": 8, "herb": False},
            {"id": 48, "name": "Fred", "colour": "human", "count": 4, "herb": False},
            {"id": 49, "name": "Fred the Son", "colour": "human", "count": 12, "herb": False},
            {"id": 19, "name": "Garlic", "colour": "white", "count": 6, "herb": True},
            {"id": 20, "name": "Kale", "colour": "green", "count": 4, "herb": False},
            {"id": 3, "name": "Lettuce", "colour": "green", "count": 7, "herb": False},
            {"id": 40, "name": "Mint", "colour": "green", "count": 4, "herb": True},
            {"id": 43, "name": "Okra", "colour": "green", "count": 4, "herb": False},
            {"id": 18, "name": "Onion", "colour": "white", "count": 5, "herb": False},
            {"id": 36, "name": "Oregano", "colour": "green", "count": 7, "herb": True},
            {"id": 39, "name": "Parsley", "colour": "green", "count": 7, "herb": True},
            {"id": 22, "name": "Parsnips", "colour": "white", "count": 8, "herb": False},
            {"id": 23, "name": "Peas", "colour": "green", "count": 4, "herb": False},
            {"id": 25, "name": "Potatoes", "colour": "white", "count": 8, "herb": False},
        ],
        [
            {"id": 26, "name": "Pumpkins", "colour": "orange", "count": 8, "herb": False},
            {"id": 27, "name": "Radishes", "colour": "red", "count": 8, "herb": False},
            {"id": 28, "name": "Rhubarb", "colour": "red", "count": 7, "herb": False},
            {"id": 37, "name": "Rosemary", "colour": "green", "count": 8, "herb": True},
            {"id": 41, "name": "Sage", "colour": "green", "count": 4, "herb": True},
            {"id": 29, "name": "Spinach", "colour": "green", "count": 7, "herb": False},
            {"id": 30, "name": "Summer Squash", "colour": "yellow", "count": 12, "herb": False},
            {"id": 16, "name": "Sweet Corn", "colour": "yellow", "count": 10, "herb": False},
            {"id": 44, "name": "Sweet Potato", "colour": "orange", "count": 12, "herb": False},
            {"id": 42, "name": "Tarragon", "colour": "green", "count": 8, "herb": True},
            {"id": 35, "name": "Thyme", "colour": "green", "count": 5, "herb": True},
            {"id": 1, "name": "Tomatoes", "colour": "red", "count": 8, "herb": False},
            {"id": 32, "name": "Turnips", "colour": "white", "count": 7, "herb": False},
            {"id": 33, "name": "Watermelon", "colour": "red", "count": 10, "herb": False},
            {"id": 34, "name": "Winter Squash", "colour": "orange", "count": 13, "herb": False},
            "",
        ],
    ]


def padded_columns_4():
    """
    Columns with 4 entries where some entries are blank to fill shorter columns to match the longest
    Used in parametrized fixture "padded_columns"
    """
    return [
        [
            {"id": 5, "name": "Asparagus", "colour": "green", "count": 9, "herb": False},
            {"id": 2, "name": "Basil", "colour": "green", "count": 5, "herb": True},
            {"id": 6, "name": "Beans", "colour": "yellow", "count": 5, "herb": False},
            {"id": 7, "name": "Beets", "colour": "red", "count": 5, "herb": False},
        ],
        [
            {"id": 15, "name": "Cucumbers", "colour": "green", "count": 9, "herb": False},
            {"id": 45, "name": "Dill", "colour": "green", "count": 4, "herb": True},
            {"id": 17, "name": "Eggplant", "colour": "purple", "count": 8, "herb": False},
            {"id": 48, "name": "Fred", "colour": "human", "count": 4, "herb": False},
        ],
        [
            {"id": 26, "name": "Pumpkins", "colour": "orange", "count": 8, "herb": False},
            {"id": 27, "name": "Radishes", "colour": "red", "count": 8, "herb": False},
            {"id": 28, "name": "Rhubarb", "colour": "red", "count": 7, "herb": False},
            "",
        ],
    ]


@pytest.fixture(params=[(padded_columns_4(), 4, 3), (padded_columns_16(), 16, 3)])
def padded_columns(request):
    """Pytest parametrized fixture to return the listed fixtures"""
    return request.param


@pytest.fixture()
def fixture_padded_columns_4():
    """Columns with 4 entries where some entries are blank to fill shorter columns to match the longest"""
    return [
        [
            {"id": 5, "name": "Asparagus", "colour": "green", "count": 9, "herb": False},
            {"id": 2, "name": "Basil", "colour": "green", "count": 5, "herb": True},
            {"id": 6, "name": "Beans", "colour": "yellow", "count": 5, "herb": False},
            {"id": 7, "name": "Beets", "colour": "red", "count": 5, "herb": False},
        ],
        [
            {"id": 15, "name": "Cucumbers", "colour": "green", "count": 9, "herb": False},
            {"id": 45, "name": "Dill", "colour": "green", "count": 4, "herb": True},
            {"id": 17, "name": "Eggplant", "colour": "purple", "count": 8, "herb": False},
            {"id": 48, "name": "Fred", "colour": "human", "count": 4, "herb": False},
        ],
        [
            {"id": 26, "name": "Pumpkins", "colour": "orange", "count": 8, "herb": False},
            {"id": 27, "name": "Radishes", "colour": "red", "count": 8, "herb": False},
            {"id": 28, "name": "Rhubarb", "colour": "red", "count": 7, "herb": False},
            "",
        ],
        4,
        3,
    ]


@pytest.fixture()
def fixture_padded_columns_16():
    """Columns with 16 entries where some entries are blank to fill shorter columns to match the longest"""
    return [
        [
            {"id": 5, "name": "Asparagus", "colour": "green", "count": 9, "herb": False},
            {"id": 2, "name": "Basil", "colour": "green", "count": 5, "herb": True},
            {"id": 6, "name": "Beans", "colour": "yellow", "count": 5, "herb": False},
            {"id": 7, "name": "Beets", "colour": "red", "count": 5, "herb": False},
            {"id": 24, "name": "Bell Peppers", "colour": "red", "count": 12, "herb": False},
            {"id": 8, "name": "Broccoli", "colour": "green", "count": 8, "herb": False},
            {"id": 9, "name": "Brussels Sprouts", "colour": "green", "count": 16, "herb": False},
            {"id": 10, "name": "Cabbage", "colour": "green", "count": 7, "herb": False},
            {"id": 21, "name": "Cantaloupe", "colour": "orange", "count": 10, "herb": False},
            {"id": 4, "name": "Carrots", "colour": "orange", "count": 7, "herb": False},
            {"id": 11, "name": "Cauliflower", "colour": "white", "count": 11, "herb": False},
            {"id": 12, "name": "Celery", "colour": "green", "count": 6, "herb": False},
            {"id": 31, "name": "Chard", "colour": "green", "count": 5, "herb": False},
            {"id": 13, "name": "Chives", "colour": "green", "count": 6, "herb": True},
            {"id": 38, "name": "Cilantro", "colour": "green", "count": 8, "herb": True},
            {"id": 14, "name": "Collard Greens", "colour": "green", "count": 14, "herb": False},
        ],
        [
            {"id": 15, "name": "Cucumbers", "colour": "green", "count": 9, "herb": False},
            {"id": 45, "name": "Dill", "colour": "green", "count": 4, "herb": True},
            {"id": 17, "name": "Eggplant", "colour": "purple", "count": 8, "herb": False},
            {"id": 48, "name": "Fred", "colour": "human", "count": 4, "herb": False},
            {"id": 49, "name": "Fred the Son", "colour": "human", "count": 12, "herb": False},
            {"id": 19, "name": "Garlic", "colour": "white", "count": 6, "herb": True},
            {"id": 20, "name": "Kale", "colour": "green", "count": 4, "herb": False},
            {"id": 3, "name": "Lettuce", "colour": "green", "count": 7, "herb": False},
            {"id": 40, "name": "Mint", "colour": "green", "count": 4, "herb": True},
            {"id": 43, "name": "Okra", "colour": "green", "count": 4, "herb": False},
            {"id": 18, "name": "Onion", "colour": "white", "count": 5, "herb": False},
            {"id": 36, "name": "Oregano", "colour": "green", "count": 7, "herb": True},
            {"id": 39, "name": "Parsley", "colour": "green", "count": 7, "herb": True},
            {"id": 22, "name": "Parsnips", "colour": "white", "count": 8, "herb": False},
            {"id": 23, "name": "Peas", "colour": "green", "count": 4, "herb": False},
            {"id": 25, "name": "Potatoes", "colour": "white", "count": 8, "herb": False},
        ],
        [
            {"id": 26, "name": "Pumpkins", "colour": "orange", "count": 8, "herb": False},
            {"id": 27, "name": "Radishes", "colour": "red", "count": 8, "herb": False},
            {"id": 28, "name": "Rhubarb", "colour": "red", "count": 7, "herb": False},
            {"id": 37, "name": "Rosemary", "colour": "green", "count": 8, "herb": True},
            {"id": 41, "name": "Sage", "colour": "green", "count": 4, "herb": True},
            {"id": 29, "name": "Spinach", "colour": "green", "count": 7, "herb": False},
            {"id": 30, "name": "Summer Squash", "colour": "yellow", "count": 12, "herb": False},
            {"id": 16, "name": "Sweet Corn", "colour": "yellow", "count": 10, "herb": False},
            {"id": 44, "name": "Sweet Potato", "colour": "orange", "count": 12, "herb": False},
            {"id": 42, "name": "Tarragon", "colour": "green", "count": 8, "herb": True},
            {"id": 35, "name": "Thyme", "colour": "green", "count": 5, "herb": True},
            {"id": 1, "name": "Tomatoes", "colour": "red", "count": 8, "herb": False},
            {"id": 32, "name": "Turnips", "colour": "white", "count": 7, "herb": False},
            {"id": 33, "name": "Watermelon", "colour": "red", "count": 10, "herb": False},
            {"id": 34, "name": "Winter Squash", "colour": "orange", "count": 13, "herb": False},
            "",
        ],
        16,
        3,
    ]


@pytest.fixture()
def columns_many():
    """Simulating many columns being returned with varying numbers of entries in each"""

    def _build_cols(num_items, num_cols):
        col = [{} for i in range(num_items - random.randint(0, num_items))]
        cols = [col for i in range(num_cols)]
        # adding one more line to ensure there is at least one line with the full num_items in it
        cols.append([{} for i in range(num_items)])
        return cols

    return _build_cols


@pytest.fixture()
def columns_same_length_4():
    """Columns are all the same length ... test will demonstrate they stay that way"""
    return [
        [   {"id": 5, "name": "Asparagus", "colour": "green", "count": 9, "herb": False},
            {"id": 2, "name": "Basil", "colour": "green", "count": 5, "herb": True},
            {"id": 6, "name": "Beans", "colour": "yellow", "count": 5, "herb": False},
            {"id": 7, "name": "Beets", "colour": "red", "count": 5, "herb": False},
        ],
        [
            {"id": 15, "name": "Cucumbers", "colour": "green", "count": 9, "herb": False},
            {"id": 45, "name": "Dill", "colour": "green", "count": 4, "herb": True},
            {"id": 17, "name": "Eggplant", "colour": "purple", "count": 8, "herb": False},
            {"id": 48, "name": "Fred", "colour": "human", "count": 4, "herb": False},
        ],
        [
            {"id": 26, "name": "Pumpkins", "colour": "orange", "count": 8, "herb": False},
            {"id": 27, "name": "Radishes", "colour": "red", "count": 8, "herb": False},
            {"id": 28, "name": "Rhubarb", "colour": "red", "count": 7, "herb": False},
            {"id": 35, "name": "Thyme", "colour": "green", "count": 5, "herb": True},
        ],
    ]


@pytest.fixture()
def first_column_empty_5():
    """First column is empty ... test will demonstrate this edge case can be handled"""
    return [
        [],
        [
            {"id": 5, "name": "Asparagus", "colour": "green", "count": 9, "herb": False},
            {"id": 2, "name": "Basil", "colour": "green", "count": 5, "herb": True},
            {"id": 6, "name": "Beans", "colour": "yellow", "count": 5, "herb": False},
            {"id": 7, "name": "Beets", "colour": "red", "count": 5, "herb": False},
            {"id": 24, "name": "Bell Peppers", "colour": "red", "count": 12, "herb": False},
        ],
        [
            {"id": 8, "name": "Broccoli", "colour": "green", "count": 8, "herb": False},        
            {"id": 15, "name": "Cucumbers", "colour": "green", "count": 9, "herb": False},
            {"id": 45, "name": "Dill", "colour": "green", "count": 4, "herb": True},
            {"id": 17, "name": "Eggplant", "colour": "purple", "count": 8, "herb": False},
            {"id": 1, "name": "Tomatoes", "colour": "red", "count": 8, "herb": False},
        ],
    ]


@pytest.fixture()
def last_column_empty_2():
    """Last column is empty ... test will demoonstrate this edge case can be handled"""
    return [
        [{"id": 5, "name": "Asparagus"}, {"id": 2, "name": "Basil"}],
        [{"id": 15, "name": "Cucumbers"}, {"id": 45, "name": "Dill"}],
        [{"id": 22, "name": "Parsnips"}, {"id": 23, "name": "Peas"}],
        [],
    ]


@pytest.fixture()
def all_columns_empty():
    """All columns are empty ... test will demoonstrate this edge case can be handled"""
    return [[] for i in range(0, 100)]


# Fixtures for specifically testing CriteriaVMCView
@pytest.fixture()
def criteria_functions_2():
    """2 functions are passed to a VMCCriteria view"""

    def a_to_m(args):
        parms = args
        return "ABCDEFGHIJKLM".find(parms[0][0]) > -1

    def n_to_z(args):
        parms = args
        return "NOPQRSTUVWXYZ".find(parms[0][0]) > -1

    return [a_to_m, n_to_z]


@pytest.fixture()
def criteria_functions_3():
    """3 functions are passed to a VMCCriteria view"""

    def a_to_m_and_count_less_than_10(args):
        """Items matching this condition go in column 1"""
        entry_keys = args
        return "ABCDEFGHIJKLM".find(entry_keys[0][0]) > -1 and entry_keys[1] < 10

    def n_to_z_and_count_10_or_greater(args):
        """Items matching this condition go in column 2"""
        entry_keys = args
        return "NOPQRSTUVWXYZ".find(entry_keys[0][0]) > -1 and entry_keys[1] >= 10

    def is_herb(args):
        """Items matching this condition go in column 3"""
        entry_keys = args
        return entry_keys[2] is True

    return [a_to_m_and_count_less_than_10, n_to_z_and_count_10_or_greater, is_herb]


@pytest.fixture()
def criteria_functions_4():
    """4 functions are passed to a VMCCriteria view"""

    def a_to_d(args):
        parms = args
        return "ABCD".find(parms[0][0]) > -1

    def e_to_m(args):
        parms = args
        return "EFGHIJKLM".find(parms[0][0]) > -1

    def n_to_r(args):
        parms = args
        return "NOPQR".find(parms[0][0]) > -1

    def s_to_z(args):
        parms = args
        return "STUVWXYZ".find(parms[0][0]) > -1

    return [a_to_d, e_to_m, n_to_r, s_to_z]


@pytest.fixture()
def criteria_functions_5():
    """5 functions are passed to a VMCCriteria view"""

    def a_to_d(args):
        parms = args
        return "ABCD".find(parms[0][0]) > -1

    def e_to_m(args):
        parms = args
        return "EFGHIJKLM".find(parms[0][0]) > -1

    def n_to_r(args):
        parms = args
        return "NOPQR".find(parms[0][0]) > -1

    def s_to_u(args):
        parms = args
        return "STU".find(parms[0][0]) > -1

    def v_to_z(args):
        parms = args
        return "VWXYZ".find(parms[0][0]) > -1

    return [a_to_d, e_to_m, n_to_r, s_to_u, v_to_z]


@pytest.fixture()
def function_args_2():
    """dictionary keys are passed"""
    return ["id", "name"]
    
@pytest.fixture()
def function_args_3():
    """dictionary keys are passed"""
    return ["name", "count", "herb"]
    
@pytest.fixture()
def function_args_4():
    """dictionary keys are passed"""
    return ["id", "name"]
    
@pytest.fixture()
def function_args_5():
    """dictionary keys are passed"""
    return ["id", "name"]    


# Fixtures specifically for testing get_queryset - common in - specific out by VMC class
@pytest.fixture()
def test_in_even_criteria_data():
    """Input data for ListView's get_queryset() override in EvenVMCView and CriteriaVMCView tests"""
    return [
        {"id": 5, "name": "Asparagus"},
        {"id": 2, "name": "Basil"},
        {"id": 6, "name": "Beans"},
        {"id": 7, "name": "Beets"},
        {"id": 24, "name": "Bell Peppers"},
        {"id": 8, "name": "Broccoli"},
        {"id": 9, "name": "Brussels Sprouts"},
        {"id": 10, "name": "Cabbage"},
        {"id": 21, "name": "Cantaloupe"},
        {"id": 4, "name": "Carrots"},
        {"id": 11, "name": "Cauliflower"},
        {"id": 12, "name": "Celery"},
        {"id": 31, "name": "Chard"},
        {"id": 13, "name": "Chives"},
        {"id": 38, "name": "Cilantro"},
        {"id": 14, "name": "Collard Greens"},
        {"id": 15, "name": "Cucumbers"},
        {"id": 45, "name": "Dill"},
        {"id": 17, "name": "Eggplant"},
        {"id": 19, "name": "Garlic"},
        {"id": 20, "name": "Kale"},
        {"id": 3, "name": "Lettuce"},
        {"id": 40, "name": "Mint"},
        {"id": 43, "name": "Okra"},
        {"id": 18, "name": "Onion"},
        {"id": 36, "name": "Oregano"},
        {"id": 39, "name": "Parsley"},
        {"id": 22, "name": "Parsnips"},
        {"id": 23, "name": "Peas"},
        {"id": 25, "name": "Potatoes"},
        {"id": 26, "name": "Pumpkins"},
        {"id": 27, "name": "Radishes"},
        {"id": 28, "name": "Rhubarb"},
        {"id": 37, "name": "Rosemary"},
        {"id": 41, "name": "Sage"},
        {"id": 29, "name": "Spinach"},
        {"id": 30, "name": "Summer Squash"},
        {"id": 16, "name": "Sweet Corn"},
        {"id": 44, "name": "Sweet Potato"},
        {"id": 42, "name": "Tarragon"},
        {"id": 35, "name": "Thyme"},
        {"id": 1, "name": "Tomatoes"},
        {"id": 32, "name": "Turnips"},
        {"id": 33, "name": "Watermelon"},
        {"id": 34, "name": "Winter Squash"},
    ]


@pytest.fixture()
def test_out_even_data():
    """"Out data for the override of ListView's get_queryset() in EvenVMCView"""
    return [
        [
            {"id": 5, "name": "Asparagus"},
            {"id": 14, "name": "Collard Greens"},
            {"id": 26, "name": "Pumpkins"},
        ],
        [
            {"id": 2, "name": "Basil"},
            {"id": 15, "name": "Cucumbers"},
            {"id": 27, "name": "Radishes"},
        ],
        [
            {"id": 6, "name": "Beans"},
            {"id": 45, "name": "Dill"},
            {"id": 28, "name": "Rhubarb"},
        ],
        [
            {"id": 7, "name": "Beets"},
            {"id": 17, "name": "Eggplant"},
            {"id": 37, "name": "Rosemary"},
        ],
        [
            {"id": 24, "name": "Bell Peppers"},
            {"id": 19, "name": "Garlic"},
            {"id": 41, "name": "Sage"},
        ],
        [
            {"id": 8, "name": "Broccoli"},
            {"id": 20, "name": "Kale"},
            {"id": 29, "name": "Spinach"},
        ],
        [
            {"id": 9, "name": "Brussels Sprouts"},
            {"id": 3, "name": "Lettuce"},
            {"id": 30, "name": "Summer Squash"},
        ],
        [
            {"id": 10, "name": "Cabbage"},
            {"id": 40, "name": "Mint"},
            {"id": 16, "name": "Sweet Corn"},
        ],
        [
            {"id": 21, "name": "Cantaloupe"},
            {"id": 43, "name": "Okra"},
            {"id": 44, "name": "Sweet Potato"},
        ],
        [
            {"id": 4, "name": "Carrots"},
            {"id": 18, "name": "Onion"},
            {"id": 42, "name": "Tarragon"},
        ],
        [
            {"id": 11, "name": "Cauliflower"},
            {"id": 36, "name": "Oregano"},
            {"id": 35, "name": "Thyme"},
        ],
        [
            {"id": 12, "name": "Celery"},
            {"id": 39, "name": "Parsley"},
            {"id": 1, "name": "Tomatoes"},
        ],
        [
            {"id": 31, "name": "Chard"},
            {"id": 22, "name": "Parsnips"},
            {"id": 32, "name": "Turnips"},
        ],
        [
            {"id": 13, "name": "Chives"},
            {"id": 23, "name": "Peas"},
            {"id": 33, "name": "Watermelon"},
        ],
        [
            {"id": 38, "name": "Cilantro"},
            {"id": 25, "name": "Potatoes"},
            {"id": 34, "name": "Winter Squash"},
        ],
    ]


@pytest.fixture()
def test_out_criteria_data():
    """"Out data for the override of ListView's get_queryset() in CriteriaVMCView"""
    return [
        [
            {"id": "5", "name": "Asparagus"},
            {"id": "19", "name": "Garlic"},
            {"id": "42", "name": "Tarragon"},
        ],
        [
            {"id": "2", "name": "Basil"},
            {"id": "20", "name": "Kale"},
            {"id": "35", "name": "Thyme"},
        ],
        [
            {"id": "6", "name": "Beans"},
            {"id": "3", "name": "Lettuce"},
            {"id": "1", "name": "Tomatoes"},
        ],
        [
            {"id": "7", "name": "Beets"},
            {"id": "40", "name": "Mint"},
            {"id": "32", "name": "Turnips"},
        ],
        [
            {"id": "24", "name": "Bell Peppers"},
            {"id": "43", "name": "Okra"},
            {"id": "33", "name": "Watermelon"},
        ],
        [
            {"id": "8", "name": "Broccoli"},
            {"id": "18", "name": "Onion"},
            {"id": "34", "name": "Winter Squash"},
        ],
        [{"id": "9", "name": "Brussels Sprouts"}, {"id": "36", "name": "Oregano"}, ""],
        [{"id": "10", "name": "Cabbage"}, {"id": "39", "name": "Parsley"}, ""],
        [{"id": "21", "name": "Cantaloupe"}, {"id": "22", "name": "Parsnips"}, ""],
        [{"id": "4", "name": "Carrots"}, {"id": "23", "name": "Peas"}, ""],
        [{"id": "11", "name": "Cauliflower"}, {"id": "25", "name": "Potatoes"}, ""],
        [{"id": "12", "name": "Celery"}, {"id": "26", "name": "Pumpkins"}, ""],
        [{"id": "31", "name": "Chard"}, {"id": "27", "name": "Radishes"}, ""],
        [{"id": "13", "name": "Chives"}, {"id": "28", "name": "Rhubarb"}, ""],
        [{"id": "38", "name": "Cilantro"}, {"id": "37", "name": "Rosemary"}, ""],
        [{"id": "14", "name": "Collard Greens"}, {"id": "41", "name": "Sage"}, ""],
        [{"id": "15", "name": "Cucumbers"}, {"id": "29", "name": "Spinach"}, ""],
        [{"id": "45", "name": "Dill"}, {"id": "30", "name": "Summer Squash"}, ""],
        [{"id": "17", "name": "Eggplant"}, {"id": "16", "name": "Sweet Corn"}, ""],
        ["", {"id": "44", "name": "Sweet Potato"}, ""],
    ]


@pytest.fixture()
def test_in_defined_data():
    """"Input data for ListView's get_queryset() override in DefinedVMCView tests"""
    return [
        [
            {"id": 5, "name": "Asparagus"},
            {"id": 2, "name": "Basil"},
            {"id": 6, "name": "Beans"},
            {"id": 7, "name": "Beets"},
            {"id": 24, "name": "Bell Peppers"},
            {"id": 8, "name": "Broccoli"},
            {"id": 9, "name": "Brussels Sprouts"},
            {"id": 10, "name": "Cabbage"},
            {"id": 21, "name": "Cantaloupe"},
        ],
        [{"id": 19, "name": "Garlic"}],
        [
            {"id": 20, "name": "Kale"},
            {"id": 3, "name": "Lettuce"},
            {"id": 40, "name": "Mint"},
            {"id": 43, "name": "Okra"},
            {"id": 18, "name": "Onion"},
            {"id": 36, "name": "Oregano"},
            {"id": 39, "name": "Parsley"},
        ],
        [
            {"id": 42, "name": "Tarragon"},
            {"id": 35, "name": "Thyme"},
            {"id": 1, "name": "Tomatoes"},
            {"id": 32, "name": "Turnips"},
            {"id": 33, "name": "Watermelon"},
            {"id": 34, "name": "Winter Squash"},
        ],
    ]


@pytest.fixture()
def test_out_defined_data():
    """"Out data for the override of ListView's get_queryset() in EvenVMCView"""
    return [
        [
            {"id": 5, "name": "Asparagus"},
            {"id": 19, "name": "Garlic"},
            {"id": 20, "name": "Kale"},
            {"id": 42, "name": "Tarragon"},
        ],
        [
            {"id": 2, "name": "Basil"},
            "",
            {"id": 3, "name": "Lettuce"},
            {"id": 35, "name": "Thyme"},
        ],
        [
            {"id": 6, "name": "Beans"},
            "",
            {"id": 40, "name": "Mint"},
            {"id": 1, "name": "Tomatoes"},
        ],
        [
            {"id": 7, "name": "Beets"},
            "",
            {"id": 43, "name": "Okra"},
            {"id": 32, "name": "Turnips"},
        ],
        [
            {"id": 24, "name": "Bell Peppers"},
            "",
            {"id": 18, "name": "Onion"},
            {"id": 33, "name": "Watermelon"},
        ],
        [
            {"id": 8, "name": "Broccoli"},
            "",
            {"id": 36, "name": "Oregano"},
            {"id": 34, "name": "Winter Squash"},
        ],
        [{"id": 9, "name": "Brussels Sprouts"}, "", {"id": 39, "name": "Parsley"}, ""],
        [{"id": 10, "name": "Cabbage"}, "", "", ""],
        [{"id": 21, "name": "Cantaloupe"}, "", "", ""],
    ]

@pytest.fixture()
def json_data_structure_with_all_data_types():
    """
    This JSON contains all the JSON data types: string, number, boolean, null/empty, object, and array.
    It was generated by calling requests and converting to Python format using .JSON method provided by requests.
    """
    return [
{'id': 1, 'title': 'hello', 'count': 35, 'boolean': True, 'empty': None, 'object': {'a': 'susan', 'b': 3}, 'array': [1, 2, 3]},
{'id': 2, 'title': 'goodbye', 'count': 42, 'boolean': False, 'empty': None, 'object': {'a': 'peter', 'b': 32}, 'array': [11, 12, 13]},
{'id': 3, 'title': 'adieu', 'count': 22, 'boolean': True, 'empty': None, 'object': {'a': 'indy', 'b': 90}, 'array': [111, 112, 113]}
]

@pytest.fixture()
def heirarchical_data_structure():
    """Heirarchical JSON data"""
    return [
        {
            "squadName": "Super hero squad",
            "homeTown": "Metro City",
            "formed": 2016,
            "secretBase": "Super tower",
            "active": True,
            "members": [
                {
                    "name": "Molecule Man",
                    "age": 29,
                    "secretIdentity": "Dan Jukes",
                    "powers": [
                        "Radiation resistance",
                        "Turning tiny",
                        "Radiation blast",
                    ],
                },
                {
                    "name": "Madame Uppercut",
                    "age": 39,
                    "secretIdentity": "Jane Wilson",
                    "powers": [
                        "Million tonne punch",
                        "Damage resistance",
                        "Superhuman reflexes",
                    ],
                },
                {
                    "name": "Eternal Flame",
                    "age": 1000000,
                    "secretIdentity": "Unknown",
                    "powers": [
                        "Immortality",
                        "Heat Immunity",
                        "Inferno",
                        "Teleportation",
                        "Interdimensional travel",
                    ],
                },
            ],
        },
        {
            "squadName": "Super hero squad2",
            "homeTown": "Toronto",
            "formed": 2020,
            "secretBase": "Super tower",
            "active": False,
            "members": [
                {
                    "name": "Molecule Man",
                    "age": 29,
                    "secretIdentity": "Dan Jukes",
                    "powers": [
                        "Radiation resistance",
                        "Turning tiny",
                        "Radiation blast",
                    ],
                },
                {
                    "name": "Madame Uppercut",
                    "age": 39,
                    "secretIdentity": "Jane Wilson",
                    "powers": [
                        "Million tonne punch",
                        "Damage resistance",
                        "Superhuman reflexes",
                    ],
                },
                {
                    "name": "Eternal Flame",
                    "age": 1000000,
                    "secretIdentity": "Unknown",
                    "powers": [
                        "Immortality",
                        "Heat Immunity",
                        "Inferno",
                        "Teleportation",
                        "Interdimensional travel",
                    ],
                },
            ],
        },
    ]
