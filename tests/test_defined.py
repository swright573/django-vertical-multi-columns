import pytest
from vertical_multi_columns.views import DefinedVMCView
from django.core.exceptions import ImproperlyConfigured

# Testing DefinedVMCView
#   Note: Columns are passed pre-filled as they are to appear.


def test_no_columns_are_passed(settings_NUMBER_OF_COLUMNS_3):
    # The number of columns passed must correspond to the columns setting
    instance = DefinedVMCView()
    with pytest.raises(ImproperlyConfigured):
        rows = instance.process_columns(None)


def test_too_few_columns_are_passed(columns_2, settings_NUMBER_OF_COLUMNS_3):
    # The number of columns passed must correspond to the columns setting
    instance = DefinedVMCView()
    with pytest.raises(ImproperlyConfigured):
        rows = instance.process_columns(columns_2)


def test_too_many_columns_are_passed(columns_4, settings_NUMBER_OF_COLUMNS_3):
    # The number of columns passed must correspond to the columns setting
    instance = DefinedVMCView()
    with pytest.raises(ImproperlyConfigured):
        rows = instance.process_columns(columns_4)


def test_correct_number_columns_are_passed(columns_4, settings_NUMBER_OF_COLUMNS_4):
    instance = DefinedVMCView()
    rows = instance.process_columns(columns_4)
    num_cols = len(rows[0])
    assert num_cols == 4


def test_same_data_after_processing(columns_2, settings_NUMBER_OF_COLUMNS_2):
    instance = DefinedVMCView()
    rows = instance.process_columns(columns_2)
    gen_columns_from_rows = []
    for c in range(len(rows)):
        column = []
        for r in rows[c]:
            column.append(r)
        gen_columns_from_rows.append(column)
    assert gen_columns_from_rows == rows


# For next test ... class fixtures are not yet supported in pytest. Therfore I had to create this mocked version
# because overridden methods in imported classes will not execute in tests
class MockDefinedVMCView(DefinedVMCView):
    def __init__(self, **kwargs: int):
        super().__init__(**kwargs)
        self.defined_in_data = kwargs.get("in_data")

    def get_data(self):
        return self.defined_in_data


def test_get_querydata(
    test_in_defined_data, test_out_defined_data, settings_NUMBER_OF_COLUMNS_4
):
    instance = MockDefinedVMCView(num_columns=4, in_data=test_in_defined_data)
    assert instance.get_queryset() == test_out_defined_data
