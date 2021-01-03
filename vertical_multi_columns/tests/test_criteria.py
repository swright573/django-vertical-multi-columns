import pytest
from django_vertical_multi_columns.configure import CriteriaDistribution
from django.core.exceptions import ImproperlyConfigured
from django.contrib.admin.utils import flatten

# Testing CriteriaDistribution
#   Note 1: Passed criteria functions determine which entries appear in which column(s)
#   Note 2: It is up to the user to ensure their criteria functions and func_args perform as expected
#   Note 3: Some entries can appear in more than one column if the criteria functions overlap

def test_no_functions_or_args_are_passed(entries_27, settings_NUMBER_OF_COLUMNS_3):
    # The number of "criteria functions" and "func args" passed by the user must correspond to the columns setting
    with pytest.raises(ImproperlyConfigured):
        my_rows = CriteriaDistribution(entries_27, None, None).process()

def test_only_functions_are_passed(entries_27, settings_NUMBER_OF_COLUMNS_3, criteria_functions_3):
    # The number of "criteria functions" and "func args" passed by the user must correspond to the columns setting
    with pytest.raises(ImproperlyConfigured):
        my_rows = CriteriaDistribution(entries_27, criteria_functions_3, None).process()

def test_only_args_are_passed(entries_27, settings_NUMBER_OF_COLUMNS_3, function_args):
    # The number of "criteria functions" and "func args" passed by the user must correspond to the columns setting
    with pytest.raises(ImproperlyConfigured):
        my_rows = CriteriaDistribution(entries_27, None, function_args).process()

def test_no_column_setting_and_fewer_than_3_functions_are_passed(entries_27,
                                                                 settings_NUMBER_OF_COLUMNS_Null,
                                                                 criteria_functions_2,
                                                                 function_args):
    # If no column setting is specified: 3 "criteria functions" must be passed
    with pytest.raises(ImproperlyConfigured):
        my_rows = CriteriaDistribution(entries_27, criteria_functions_2, function_args).process()

def test_no_column_setting_and_more_than_3_functions_are_passed(entries_27,
                                                                settings_NUMBER_OF_COLUMNS_Null,
                                                                criteria_functions_2,
                                                                function_args):
    # If no column setting is specified: 3 "criteria functions" must be passed
    with pytest.raises(ImproperlyConfigured):
        my_rows = CriteriaDistribution(entries_27, criteria_functions_2, function_args).process()

def test_no_column_setting_and_3_functions_are_passed(entries_27,
                                                      settings_NUMBER_OF_COLUMNS_Null,
                                                      criteria_functions_3,
                                                      function_args):
    # If no setting is specified: 3 columns are generated and 3 "criteria functions"
    my_rows = CriteriaDistribution(entries_27, criteria_functions_3, function_args).process()
    my_num_cols = len(my_rows[0])
    assert my_num_cols == 3

def test_number_of_functions_same_as_columns_setting(entries_27,
                                                     settings_NUMBER_OF_COLUMNS_4,
                                                     criteria_functions_4,
                                                     function_args):
    # The number of "criteria functions" and "func args" passed by the user must correspond to the columns setting
    my_rows = CriteriaDistribution(entries_27, criteria_functions_4, function_args).process()
    my_num_cols = len(my_rows[0])
    assert my_num_cols == 4

def test_number_columns_kwarg_no_setting(entries_27, 
                                         settings_NUMBER_OF_COLUMNS_Null,
                                         criteria_functions_5,
                                         function_args):
    # the number of columns corresponds to num_columns kwarg passed
    my_rows = CriteriaDistribution(entries_27, criteria_functions_5, function_args, num_columns=5).process()
    my_num_cols = len(my_rows[0])
    assert my_num_cols == 5
    
    
def test_number_columns_kwarg_with_setting(entries_27, 
                                           settings_NUMBER_OF_COLUMNS_4,
                                           criteria_functions_5,
                                           function_args):
    # the number of columns corresponds to num_columns kwarg passed
    my_rows = CriteriaDistribution(entries_27, criteria_functions_5, function_args,num_columns=5).process()
    my_num_cols = len(my_rows[0])
    assert my_num_cols == 5
    
def test_same_entries_in_same_vertical_order(entries_27, 
                                             criteria_functions_2,
                                             function_args, 
                                             settings_NUMBER_OF_COLUMNS_2):
    # All the entries received are still there and are vertically sorted in the same order as received
    # Note entries_27 spread over 4 rows means 7 rows with the last row having 1 null entry in the last position
    # Null entries must be removed. They were just filler to complete the row.
    my_rows = CriteriaDistribution(entries_27, criteria_functions_2, function_args).process()
    temp_list = []
    for c in range(2):
        temp_list.append([my_rows[r][c]['name'] if my_rows[r][c] != '' else 'to-be-removed' for r in range(7)])
    temp_list = flatten(temp_list)
    generated_entries = [e for e in temp_list if e != 'to-be-removed']
    original_entries = [e['name'] for e in entries_27]
    