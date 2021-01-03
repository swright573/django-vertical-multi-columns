import pytest
from django_vertical_multi_columns.configure import DefinedDistribution
from django.core.exceptions import ImproperlyConfigured

# Testing DefinedDistribution
#   Note: Columns are passed pre-filled as they are to appear.

def test_no_columns_are_passed(settings_NUMBER_OF_COLUMNS_3):
    # The number of columns passed must correspond to the columns setting
    with pytest.raises(ImproperlyConfigured):
        my_rows = DefinedDistribution(None).process()

def test_too_few_columns_are_passed(columns_2, settings_NUMBER_OF_COLUMNS_3):
    # The number of columns passed must correspond to the columns setting
    with pytest.raises(ImproperlyConfigured):
        my_rows = DefinedDistribution(columns_2).process()

def test_too_many_columns_are_passed(columns_4, settings_NUMBER_OF_COLUMNS_3):
    # The number of columns passed must correspond to the columns setting
    with pytest.raises(ImproperlyConfigured):
        my_rows = DefinedDistribution(columns_4).process()

def test_correct_number_columns_are_passed(columns_4, settings_NUMBER_OF_COLUMNS_4):
    my_rows = DefinedDistribution(columns_4).process()
    my_num_cols = len(my_rows[0])
    assert my_num_cols == 4

def test_same_data_after_processing(columns_2, settings_NUMBER_OF_COLUMNS_2):
    rows = DefinedDistribution(columns_2).process()
    gen_columns_from_rows = []
    for c in range(len(rows)):
        column = []
        for r in rows[c]:
            column.append(r)
        gen_columns_from_rows.append(column)
    assert gen_columns_from_rows == rows