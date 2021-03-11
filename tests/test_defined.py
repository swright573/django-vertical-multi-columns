"""
Tests for DefinedVMCView
Note: Columns are passed pre-filled as they are to appear.
"""

import pytest
from django.core.exceptions import ImproperlyConfigured

from vertical_multi_columns.views import DefinedVMCView


def test_no_columns_are_passed(settings_number_of_columns_3):
    """An error is raised if there are no columns passed"""
    instance = DefinedVMCView()
    with pytest.raises(ImproperlyConfigured):
        instance.process_columns(None)


def test_too_few_columns_are_passed(columns_2, settings_number_of_columns_3):
    """An error is raised if too few columns are passed"""
    instance = DefinedVMCView()
    with pytest.raises(ImproperlyConfigured):
        instance.process_columns(columns_2)


def test_too_many_columns_are_passed(columns_4, settings_number_of_columns_3):
    """An error is raised if too many columns are raised"""
    instance = DefinedVMCView()
    with pytest.raises(ImproperlyConfigured):
        instance.process_columns(columns_4)


def test_correct_number_columns_are_passed(columns_4, settings_number_of_columns_4):
    """Test that the correct numbers of columns does not raise an error"""
    instance = DefinedVMCView()
    rows = instance.process_columns(columns_4)
    num_cols = len(rows[0])
    assert num_cols == 4


def test_same_data_after_processing(columns_2, settings_number_of_columns_2):
    """Test that the original data can be reconstructed from the processed data, proving the processing worked """
    instance = DefinedVMCView()
    rows = instance.process_columns(columns_2)
    gen_columns_from_rows = []
    num_columns = len(rows)
    for col in range(num_columns):
        column = []
        for row in rows[col]:
            column.append(row)
        gen_columns_from_rows.append(column)
    assert gen_columns_from_rows == rows


class MockDefinedVMCView(DefinedVMCView):
    """
    For next test ... class fixtures are not yet supported in pytest. Therfore I had to create this mocked version
    because overridden methods in imported classes will not execute in tests
    """

    def __init__(self, **kwargs: int):
        super().__init__(**kwargs)
        self.defined_in_data = kwargs.get("in_data")

    def get_data(self):
        return self.defined_in_data


def test_get_querydata(test_in_defined_data, test_out_defined_data, settings_number_of_columns_4):
    """Test that overriding get_queryset() works"""
    instance = MockDefinedVMCView(num_columns=4, in_data=test_in_defined_data)
    assert instance.get_queryset() == test_out_defined_data
