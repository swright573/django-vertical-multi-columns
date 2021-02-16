"""
Tests for CriteriaVMCView
Note 1: Passed criteria functions determine which entries appear in which column(s)
Note 2: It is up to the user to ensure their criteria functions and func_args perform as expected
Note 3: Some entries can appear in more than one column if the criteria functions overlap
"""

import pytest
from django.core.exceptions import ImproperlyConfigured
from django.contrib.admin.utils import flatten
from vertical_multi_columns.views import CriteriaVMCView


def test_no_functions_or_args_are_passed(settings_number_of_columns_3):
    """The number of "criteria functions" and "func args" passed by the user must correspond to the columns setting"""
    instance = CriteriaVMCView()
    with pytest.raises(ImproperlyConfigured):
        instance.check_criteria([], [])


def test_only_functions_are_passed(settings_number_of_columns_3, criteria_functions_3):
    """The number of "criteria functions" and "func args" passed by the user must correspond to the columns setting"""
    instance = CriteriaVMCView()
    with pytest.raises(ImproperlyConfigured):
        instance.check_criteria(criteria_functions_3, None)


def test_only_args_are_passed(function_args):
    """func args must passed by the user"""
    instance = CriteriaVMCView()
    with pytest.raises(ImproperlyConfigured):
        instance.check_criteria(None, function_args)


def test_no_column_setting_and_fewer_than_3_functions_are_passed(
    settings_number_of_columns_null, criteria_functions_2, function_args
):
    """If no column setting is specified: 3 "criteria functions" must be passed"""
    instance = CriteriaVMCView()
    with pytest.raises(ImproperlyConfigured):
        instance.check_criteria(criteria_functions_2, function_args)


def test_no_column_setting_and_more_than_3_functions_are_passed(
    settings_number_of_columns_null, criteria_functions_4, function_args
):
    """If no column setting is specified: 3 "criteria functions" must be passed"""
    instance = CriteriaVMCView()
    with pytest.raises(ImproperlyConfigured):
        instance.check_criteria(criteria_functions_4, function_args)


def test_no_column_setting_and_3_functions_are_passed(
    settings_number_of_columns_null, entries_27, criteria_functions_3, function_args
):
    """If no setting is specified: 3 columns are generated and 3 criteria functions"""
    instance = CriteriaVMCView()
    rows = instance.process_entries(entries_27, criteria_functions_3, function_args)
    num_cols = len(rows[0])
    assert num_cols == 3


def test_number_of_functions_same_as_columns_setting(
    settings_number_of_columns_4, entries_27, criteria_functions_4, function_args
):
    """The number of "criteria functions" and "func args" passed by the user must correspond to the columns setting"""
    instance = CriteriaVMCView()
    rows = instance.process_entries(entries_27, criteria_functions_4, function_args)
    num_cols = len(rows[0])
    assert num_cols == 4


def test_number_columns_kwarg_no_setting(settings_number_of_columns_null, entries_27, criteria_functions_5, function_args):
    """the number of columns corresponds to num_columns kwarg passed"""
    instance = CriteriaVMCView(num_columns=5)
    rows = instance.process_entries(entries_27, criteria_functions_5, function_args)
    num_cols = len(rows[0])
    assert num_cols == 5


def test_number_columns_kwarg_with_setting(entries_27, settings_number_of_columns_4, criteria_functions_5, function_args):
    """the number of columns corresponds to num_columns kwarg passed"""
    instance = CriteriaVMCView(num_columns=5)
    rows = instance.process_entries(entries_27, criteria_functions_5, function_args)
    num_cols = len(rows[0])
    assert num_cols == 5


def test_same_entries_in_same_vertical_order(entries_27, criteria_functions_2, function_args, settings_number_of_columns_2):
    """
    All the entries received are still there and are vertically sorted in the same order as received
    Note entries_27 spread over 4 rows means 7 rows with the last row having 1 null entry in the last position
    Null entries must be removed. They were just filler to complete the row.
    """

    instance = CriteriaVMCView()
    rows = instance.process_entries(entries_27, criteria_functions_2, function_args)
    temp_list = []
    for col in range(2):  # hard coded 2 because I know this will generate 2 columns
        temp_list.append([rows[row][col]["name"] if rows[row][col] != "" else "to-be-removed" for row in range(len(rows))])
    temp_list = flatten(temp_list)
    generated_entries = [entry for entry in temp_list if entry != "to-be-removed"]
    original_entries = [entry["name"] for entry in entries_27]
    assert generated_entries == original_entries


class MockCriteriaVMCView(CriteriaVMCView):
    """
    For next test ... class fixtures are not yet supported in pytest. Therfore I had to create this mocked version
    because overridden methods in imported classes will not execute in tests
    """

    def __init__(self, **kwargs: int):
        super().__init__(**kwargs)
        self.in_data = kwargs.get("in_data")

    def get_data(self):
        return self.in_data

    def get_column_criteria(self):
        def aaa_to_fff(args):
            parms = args.split(",")
            return "ABCDEF".find(parms[0][0]) > -1

        def ggg_to_sss(args):
            parms = args.split(",")
            return "GHIJKLMNOPQRS".find(parms[0][0]) > -1

        def ttt_to_zzz(args):
            parms = args.split(",")
            return "TUVWXYZ".find(parms[0][0]) > -1

        return [aaa_to_fff, ggg_to_sss, ttt_to_zzz], ["name", "id"]


def test_get_querydata(test_in_even_criteria_data, test_out_criteria_data, settings_number_of_columns_3):
    """Test that overriding get_queryset() works"""
    instance = MockCriteriaVMCView(in_data=test_in_even_criteria_data)
    assert instance.get_queryset() == test_out_criteria_data
