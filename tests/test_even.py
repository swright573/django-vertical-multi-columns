import pytest
from vertical_multi_columns.views import EvenVMCView
from django.contrib.admin.utils import flatten

#   Testing EvenVMCView

def test_number_columns_correct(entries_27, settings_NUMBER_OF_COLUMNS_3):
    # the number of columns generated corresponds to the column number setting
    instance = EvenVMCView()
    rows = instance.process_entries(entries_27)
    num_cols = len(rows[0])
    assert num_cols == 3

def test_number_columns_defaults_to_3(entries_27, settings_NUMBER_OF_COLUMNS_Null):
    # the number of columns defaults to 3 if not provided
    instance = EvenVMCView()
    rows = instance.process_entries(entries_27)
    num_cols = len(rows[0])
    assert num_cols == 3
    
def test_number_columns_kwarg_no_setting(entries_27, settings_NUMBER_OF_COLUMNS_Null):
    # the number of columns corresponds to num_columns kwarg passed
    instance = EvenVMCView(num_columns=5)
    rows = instance.process_entries(entries_27)
    num_cols = len(rows[0])
    assert num_cols == 5
    
def test_number_columns_kwarg_with_setting(entries_27, settings_NUMBER_OF_COLUMNS_4):
    # the number of columns corresponds to num_columns kwarg passed
    instance = EvenVMCView(num_columns=5)
    rows = instance.process_entries(entries_27)
    num_cols = len(rows[0])
    assert num_cols == 5

def test_same_entries_in_same_vertical_order(entries_27, settings_NUMBER_OF_COLUMNS_4):
    # All the entries received are still there and are vertically sorted in the same order as received
    # Note entries_27 spread over 4 rows means 7 rows with the last row having 1 null entry in the last position
    # Null entries must be removed. They were just filler to complete the row and keep the template happy.
    instance = EvenVMCView()
    rows = instance.process_entries(entries_27)
    temp_list = []
    for c in range(4):
        temp_list.append([rows[r][c]['name'] if rows[r][c] != '' else 'to-be-removed' for r in range(7)])
    temp_list = flatten(temp_list)
    generated_entries = [e for e in temp_list if e != 'to-be-removed']
    original_entries = [e['name'] for e in entries_27]

    assert original_entries == generated_entries

def test_partial_rows_display_data_in_left_most_columns(entries_27, settings_NUMBER_OF_COLUMNS_5):
    # As above, when the number of entries to be displayed does not divide evenly by the number of columns,
    # the extra cells are displayed in the left most columns of the last row
    # The 27 entries spread over 5 columns means 6 rows. The first 5 rows should have dictionaries in all positions.
    # The last row should have only 2 dictionaries in the first 2 positions. The remaining 3 should be empty strings.
    # This test checks for this.
    instance = EvenVMCView()
    rows = instance.process_entries(entries_27)
    for r in range(len(rows) - 1):
        row = rows[r]
        for c in row:
            for i in range(5):
                assert type(row[i]) is dict
    row = rows[len(rows)-1]
    for i in range(2):
        assert type(row[i]) is dict
    for i in range(2, 5):
        assert row[i] == ''

# for next test ... class fixtures not yet supported in pytest
# note ... I had to create this mocked version because overridden methods would not execute in tests
class MockEvenVMCView(EvenVMCView):
    def __init__(self, **kwargs: int):
        super().__init__(**kwargs)
        self.set_number_of_columns(**kwargs)
        self.in_data = kwargs.get('in_data')

    def get_data(self):
        return self.in_data

def test_get_querydata(test_in_even_criteria_data, test_out_even_data, settings_NUMBER_OF_COLUMNS_3):
    instance = MockEvenVMCView(in_data=test_in_even_criteria_data)
    assert instance.get_queryset() == test_out_even_data
