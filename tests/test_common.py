"""
Tests for common elements found in _BaseVMCView
"""

import pytest

from vertical_multi_columns.views import EvenVMCView, _BaseVMC

# Testing method pad_columns
#   What to test
#   The method "pad_columns" generates columns equal in length to the longest column
#   - all columns already equal
#   - all columns empty
#   - first column empty
#   - last column empty
#   - lots of columns


def test_pad_columns_already_same(columns_same_length_4):
    """Ensure columns already the same length are not padded any further"""
    instance = _BaseVMC()
    columns, max_column = instance.pad_columns(columns_same_length_4)
    assert max_column == 4
    for i in columns:
        assert (len(i)) == 4


def test_pad_first_column_empty(first_column_empty_5):
    """Ensure edge case where first column in empty is padded correctly"""
    instance = _BaseVMC()
    columns, max_column = instance.pad_columns(first_column_empty_5)
    assert max_column == 5
    for i in columns:
        assert (len(i)) == 5


def test_pad_all_columns_empty(all_columns_empty):
    """Ensure edge case where all columns are empty can be handled"""
    instance = _BaseVMC()
    columns, max_column = instance.pad_columns(all_columns_empty)
    assert max_column == 0
    for i in columns:
        assert (len(i)) == 0


def test_pad_last_column_empty(last_column_empty_2):
    """Ensure edge case where last column in empty is padded correctly"""
    instance = _BaseVMC()
    columns, max_column = instance.pad_columns(last_column_empty_2)
    assert max_column == 2
    for i in columns:
        assert (len(i)) == 2


def test_pad_lots_of_columns(columns_many):
    """Ensure edge case where there are more columns than would be normally expected are handled correctly"""
    instance = _BaseVMC()
    columns, max_column = instance.pad_columns(columns_many(1000, 5000))
    assert max_column == 1000
    for i in columns:
        assert (len(i)) == 1000


# Testing method build_new_rows
#   What to test
#   The method "build_new_rows" generates a set of rows that correspond vertically to the passed columns
#   - number of rows corresponds to max_column value
#   - each row contains the number of elements specified by the setting number_of_columns
#   - values in rows are the same as the corresponding cell in columns

# The next two tests are verifying the same thing.
# I've included them for my own documentation.
# They demonstrate using a parametrized fixture versus passing multiple fixtures with getfixturevalue()

# NB ... In some cases, I'm instantiating EvenVMCView to get access to _BaseVMCView methods for testing since
# that is the only way I can pass in number_of_columns


def test_build_using_parametrized_fixture(padded_columns):
    """Ensure rows are built correctly. Using one method for parametrized fixtures."""
    original_columns = padded_columns[0]
    out_column_length = padded_columns[1]
    num_cols = padded_columns[2]
    instance = EvenVMCView(num_columns=num_cols)  # using EvenVMCView but for test, only interested in _BaseVMC
    rows = instance.build_new_rows(original_columns, out_column_length)

    assert len(rows) == out_column_length  # number of rows corresponds to max length of the original columns
    for row in rows:
        assert (
            len(row) == instance.number_of_columns
        )  # each row contains the number of elements specified by the setting number_of_columns

    SUSAN - Rework this
    reversed_columns = []
    for num in range(instance.number_of_columns):
        col = [rows[row][num] for row in range(out_column_length)]
        reversed_columns.append(col)
    assert reversed_columns == original_columns  # when "unbuilt" the result should be identical to the original columns


@pytest.mark.parametrize("padded_columns", [("fixture_padded_columns_4"), ("fixture_padded_columns_16")])
def test_build_using_getfixturevalue(padded_columns, request):
    """Ensure rows are built correctly. This is the same test as above using a different method of parametrizing fixtures"""
    padded_columns = request.getfixturevalue(padded_columns)
    original_columns = padded_columns[0]
    out_column_length = padded_columns[1]
    num_cols = padded_columns[2]
    instance = EvenVMCView(num_columns=num_cols)  # using EvenVMCView but for test, only interested in _BaseVMC
    rows = instance.build_new_rows(original_columns, out_column_length)

    assert len(rows) == out_column_length  # number of rows corresponds to max length of the original columns
    for row in rows:
        assert (
            len(row) == instance.number_of_columns
        )  # each row contains the number of elements specified by the setting number_of_columns
    
    SUSAN - Rework this
    reversed_columns = []
    for num in range(instance.number_of_columns):
        col = [rows[row][num] for row in range(out_column_length)]
        reversed_columns.append(col)
    assert reversed_columns == original_columns  # when "unbuilt" the result should be identical to the original columns
