"""
Tests for examplesite
"""

import pytest

from example_site import views


@pytest.fixture()
def in_data_even_and_criteria_views():
    """In data for all views being tested """
    return [
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
        {"id": 15, "name": "Cucumbers", "colour": "green", "count": 9, "herb": False},
        {"id": 45, "name": "Dill", "colour": "green", "count": 4, "herb": True},
        {"id": 17, "name": "Eggplant", "colour": "purple", "count": 8, "herb": False},
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
    ]


@pytest.fixture()
def out_even_simple_rows():
    """Output rows for example even view"""
    return [
        [
            {"id": 5, "name": "Asparagus", "colour": "green", "count": 9, "herb": False},
            {"id": 4, "name": "Carrots", "colour": "orange", "count": 7, "herb": False},
            {"id": 17, "name": "Eggplant", "colour": "purple", "count": 8, "herb": False},
            {"id": 22, "name": "Parsnips", "colour": "white", "count": 8, "herb": False},
            {"id": 30, "name": "Summer Squash", "colour": "yellow", "count": 12, "herb": False},
        ],
        [
            {"id": 2, "name": "Basil", "colour": "green", "count": 5, "herb": True},
            {"id": 11, "name": "Cauliflower", "colour": "white", "count": 11, "herb": False},
            {"id": 19, "name": "Garlic", "colour": "white", "count": 6, "herb": True},
            {"id": 23, "name": "Peas", "colour": "green", "count": 4, "herb": False},
            {"id": 16, "name": "Sweet Corn", "colour": "yellow", "count": 10, "herb": False},
        ],
        [
            {"id": 6, "name": "Beans", "colour": "yellow", "count": 5, "herb": False},
            {"id": 12, "name": "Celery", "colour": "green", "count": 6, "herb": False},
            {"id": 20, "name": "Kale", "colour": "green", "count": 4, "herb": False},
            {"id": 25, "name": "Potatoes", "colour": "white", "count": 8, "herb": False},
            {"id": 44, "name": "Sweet Potato", "colour": "orange", "count": 12, "herb": False},
        ],
        [
            {"id": 7, "name": "Beets", "colour": "red", "count": 5, "herb": False},
            {"id": 31, "name": "Chard", "colour": "green", "count": 5, "herb": False},
            {"id": 3, "name": "Lettuce", "colour": "green", "count": 7, "herb": False},
            {"id": 26, "name": "Pumpkins", "colour": "orange", "count": 8, "herb": False},
            {"id": 42, "name": "Tarragon", "colour": "green", "count": 8, "herb": True},
        ],
        [
            {"id": 24, "name": "Bell Peppers", "colour": "red", "count": 12, "herb": False},
            {"id": 13, "name": "Chives", "colour": "green", "count": 6, "herb": True},
            {"id": 40, "name": "Mint", "colour": "green", "count": 4, "herb": True},
            {"id": 27, "name": "Radishes", "colour": "red", "count": 8, "herb": False},
            {"id": 35, "name": "Thyme", "colour": "green", "count": 5, "herb": True},
        ],
        [
            {"id": 8, "name": "Broccoli", "colour": "green", "count": 8, "herb": False},
            {"id": 38, "name": "Cilantro", "colour": "green", "count": 8, "herb": True},
            {"id": 43, "name": "Okra", "colour": "green", "count": 4, "herb": False},
            {"id": 28, "name": "Rhubarb", "colour": "red", "count": 7, "herb": False},
            {"id": 1, "name": "Tomatoes", "colour": "red", "count": 8, "herb": False},
        ],
        [
            {"id": 9, "name": "Brussels Sprouts", "colour": "green", "count": 16, "herb": False},
            {"id": 14, "name": "Collard Greens", "colour": "green", "count": 14, "herb": False},
            {"id": 18, "name": "Onion", "colour": "white", "count": 5, "herb": False},
            {"id": 37, "name": "Rosemary", "colour": "green", "count": 8, "herb": True},
            {"id": 32, "name": "Turnips", "colour": "white", "count": 7, "herb": False},
        ],
        [
            {"id": 10, "name": "Cabbage", "colour": "green", "count": 7, "herb": False},
            {"id": 15, "name": "Cucumbers", "colour": "green", "count": 9, "herb": False},
            {"id": 36, "name": "Oregano", "colour": "green", "count": 7, "herb": True},
            {"id": 41, "name": "Sage", "colour": "green", "count": 4, "herb": True},
            {"id": 33, "name": "Watermelon", "colour": "red", "count": 10, "herb": False},
        ],
        [
            {"id": 21, "name": "Cantaloupe", "colour": "orange", "count": 10, "herb": False},
            {"id": 45, "name": "Dill", "colour": "green", "count": 4, "herb": True},
            {"id": 39, "name": "Parsley", "colour": "green", "count": 7, "herb": True},
            {"id": 29, "name": "Spinach", "colour": "green", "count": 7, "herb": False},
            {"id": 34, "name": "Winter Squash", "colour": "orange", "count": 13, "herb": False},
        ],
    ]


@pytest.fixture()
def out_criteria_simple_rows():
    """Output rows for example criteria view"""
    return [
        [
            {"id": 5, "name": "Asparagus", "colour": "green", "count": 9, "herb": False},
            {"id": 30, "name": "Summer Squash", "colour": "yellow", "count": 12, "herb": False},
            {"id": 2, "name": "Basil", "colour": "green", "count": 5, "herb": True},
        ],
        [
            {"id": 2, "name": "Basil", "colour": "green", "count": 5, "herb": True},
            {"id": 16, "name": "Sweet Corn", "colour": "yellow", "count": 10, "herb": False},
            {"id": 13, "name": "Chives", "colour": "green", "count": 6, "herb": True},
        ],
        [
            {"id": 6, "name": "Beans", "colour": "yellow", "count": 5, "herb": False},
            {"id": 44, "name": "Sweet Potato", "colour": "orange", "count": 12, "herb": False},
            {"id": 38, "name": "Cilantro", "colour": "green", "count": 8, "herb": True},
        ],
        [
            {"id": 7, "name": "Beets", "colour": "red", "count": 5, "herb": False},
            {"id": 33, "name": "Watermelon", "colour": "red", "count": 10, "herb": False},
            {"id": 45, "name": "Dill", "colour": "green", "count": 4, "herb": True},
        ],
        [
            {"id": 8, "name": "Broccoli", "colour": "green", "count": 8, "herb": False},
            {"id": 34, "name": "Winter Squash", "colour": "orange", "count": 13, "herb": False},
            {"id": 19, "name": "Garlic", "colour": "white", "count": 6, "herb": True},
        ],
        [
            {"id": 10, "name": "Cabbage", "colour": "green", "count": 7, "herb": False},
            "",
            {"id": 40, "name": "Mint", "colour": "green", "count": 4, "herb": True},
        ],
        [
            {"id": 4, "name": "Carrots", "colour": "orange", "count": 7, "herb": False},
            "",
            {"id": 36, "name": "Oregano", "colour": "green", "count": 7, "herb": True},
        ],
        [
            {"id": 12, "name": "Celery", "colour": "green", "count": 6, "herb": False},
            "",
            {"id": 39, "name": "Parsley", "colour": "green", "count": 7, "herb": True},
        ],
        [
            {"id": 31, "name": "Chard", "colour": "green", "count": 5, "herb": False},
            "",
            {"id": 37, "name": "Rosemary", "colour": "green", "count": 8, "herb": True},
        ],
        [
            {"id": 13, "name": "Chives", "colour": "green", "count": 6, "herb": True},
            "",
            {"id": 41, "name": "Sage", "colour": "green", "count": 4, "herb": True},
        ],
        [
            {"id": 38, "name": "Cilantro", "colour": "green", "count": 8, "herb": True},
            "",
            {"id": 42, "name": "Tarragon", "colour": "green", "count": 8, "herb": True},
        ],
        [
            {"id": 15, "name": "Cucumbers", "colour": "green", "count": 9, "herb": False},
            "",
            {"id": 35, "name": "Thyme", "colour": "green", "count": 5, "herb": True},
        ],
        [{"id": 45, "name": "Dill", "colour": "green", "count": 4, "herb": True}, "", ""],
        [{"id": 17, "name": "Eggplant", "colour": "purple", "count": 8, "herb": False}, "", ""],
        [{"id": 19, "name": "Garlic", "colour": "white", "count": 6, "herb": True}, "", ""],
        [{"id": 20, "name": "Kale", "colour": "green", "count": 4, "herb": False}, "", ""],
        [{"id": 3, "name": "Lettuce", "colour": "green", "count": 7, "herb": False}, "", ""],
        [{"id": 40, "name": "Mint", "colour": "green", "count": 4, "herb": True}, "", ""],
    ]


@pytest.fixture()
def simple_criteria_functions_3():
    """Criteria functions for TBD"""

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

    return [a_to_m_and_count_less_than_10, n_to_z_and_count_10_or_greater, is_herb]


@pytest.fixture()
def simple_function_args_3():
    """Arguments for criteria functions"""
    return ["name", "count", "herb"]


@pytest.fixture()
def out_defined_rows():
    """Output rows for example defined view"""
    return [
        [
            {"id": 8, "name": "Broccoli", "colour": "green", "count": 8, "herb": False},
            {"id": 5, "name": "Asparagus", "colour": "green", "count": 9, "herb": False},
            {"id": 11, "name": "Cauliflower", "colour": "white", "count": 11, "herb": False},
            {"id": 6, "name": "Beans", "colour": "yellow", "count": 5, "herb": False},
        ],
        [
            {"id": 9, "name": "Brussels Sprouts", "colour": "green", "count": 16, "herb": False},
            {"id": 2, "name": "Basil", "colour": "green", "count": 5, "herb": True},
            {"id": 12, "name": "Celery", "colour": "green", "count": 6, "herb": False},
            {"id": 7, "name": "Beets", "colour": "red", "count": 5, "herb": False},
        ],
        [
            {"id": 10, "name": "Cabbage", "colour": "green", "count": 7, "herb": False},
            {"id": 3, "name": "Lettuce", "colour": "green", "count": 7, "herb": False},
            {"id": 31, "name": "Chard", "colour": "green", "count": 5, "herb": False},
            {"id": 24, "name": "Bell Peppers", "colour": "red", "count": 12, "herb": False},
        ],
        [
            {"id": 38, "name": "Cilantro", "colour": "green", "count": 8, "herb": True},
            {"id": 40, "name": "Mint", "colour": "green", "count": 4, "herb": True},
            {"id": 36, "name": "Oregano", "colour": "green", "count": 7, "herb": True},
            {"id": 21, "name": "Cantaloupe", "colour": "orange", "count": 10, "herb": False},
        ],
        [
            {"id": 14, "name": "Collard Greens", "colour": "green", "count": 14, "herb": False},
            {"id": 43, "name": "Okra", "colour": "green", "count": 4, "herb": False},
            {"id": 39, "name": "Parsley", "colour": "green", "count": 7, "herb": True},
            {"id": 4, "name": "Carrots", "colour": "orange", "count": 7, "herb": False},
        ],
        [
            {"id": 15, "name": "Cucumbers", "colour": "green", "count": 9, "herb": False},
            {"id": 37, "name": "Rosemary", "colour": "green", "count": 8, "herb": True},
            {"id": 1, "name": "Tomatoes", "colour": "red", "count": 8, "herb": False},
            {"id": 13, "name": "Chives", "colour": "green", "count": 6, "herb": True},
        ],
        [
            {"id": 45, "name": "Dill", "colour": "green", "count": 4, "herb": True},
            {"id": 41, "name": "Sage", "colour": "green", "count": 4, "herb": True},
            {"id": 32, "name": "Turnips", "colour": "white", "count": 7, "herb": False},
            {"id": 19, "name": "Garlic", "colour": "white", "count": 6, "herb": True},
        ],
        [
            {"id": 17, "name": "Eggplant", "colour": "purple", "count": 8, "herb": False},
            {"id": 29, "name": "Spinach", "colour": "green", "count": 7, "herb": False},
            {"id": 33, "name": "Watermelon", "colour": "red", "count": 10, "herb": False},
            {"id": 20, "name": "Kale", "colour": "green", "count": 4, "herb": False},
        ],
        [
            {"id": 22, "name": "Parsnips", "colour": "white", "count": 8, "herb": False},
            {"id": 30, "name": "Summer Squash", "colour": "yellow", "count": 12, "herb": False},
            {"id": 34, "name": "Winter Squash", "colour": "orange", "count": 13, "herb": False},
            {"id": 18, "name": "Onion", "colour": "white", "count": 5, "herb": False},
        ],
        [
            {"id": 23, "name": "Peas", "colour": "green", "count": 4, "herb": False},
            {"id": 16, "name": "Sweet Corn", "colour": "yellow", "count": 10, "herb": False},
            "",
            {"id": 28, "name": "Rhubarb", "colour": "red", "count": 7, "herb": False},
        ],
        [
            {"id": 25, "name": "Potatoes", "colour": "white", "count": 8, "herb": False},
            "",
            "",
            {"id": 44, "name": "Sweet Potato", "colour": "orange", "count": 12, "herb": False},
        ],
        [
            {"id": 26, "name": "Pumpkins", "colour": "orange", "count": 8, "herb": False},
            "",
            "",
            {"id": 42, "name": "Tarragon", "colour": "green", "count": 8, "herb": True},
        ],
        [
            {"id": 27, "name": "Radishes", "colour": "red", "count": 8, "herb": False},
            "",
            "",
            {"id": 35, "name": "Thyme", "colour": "green", "count": 5, "herb": True},
        ],
    ]


def test_even_example(in_data_even_and_criteria_views, out_even_simple_rows):
    """Even example generates expected rows"""
    instance = views.EvenVMCSimpleJson()
    rows = instance.process_entries(in_data_even_and_criteria_views)
    assert rows == out_even_simple_rows


def test_criteria_example(out_criteria_simple_rows):
    """Criteria example generates expected rows"""
    instance = views.CriteriaVMCSimpleJson()
    rows = instance.process_entries(in_data_even_and_criteria_views, simple_criteria_functions_3, simple_function_args_3)
    assert rows == out_criteria_simple_rows


def test_defined_example(out_defined_rows):
    """Defined example generates expected rows"""
    instance = views.DefinedVMC()
    in_data = instance.get_data()
    rows = instance.process_columns(in_data)
    assert rows == out_defined_rows
