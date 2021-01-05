import pytest
from vertical_multi_columns.configure import BaseVMC

# Testing method pad_columns
#   What to test
#   The method "pad_columns" generates columns of equal in length to the longest column
#   - all columns already equal
#   - all columns empty
#   - first column empty
#   - last column empty
#   - lots of columns

def test_pad_columns_already_same(entries_0, columns_same_length_4):
    instance = BaseVMC()
    columns, max_column = instance.pad_columns(columns_same_length_4)
    assert max_column == 4
    for i in columns:
        assert(len(i)) == 4

def test_pad_first_column_empty(entries_0, first_column_empty_5):
    instance = BaseVMC()
    columns, max_column = instance.pad_columns(first_column_empty_5)
    assert max_column == 5
    for i in columns:
        assert(len(i)) == 5

def test_pad_all_columns_empty(entries_0, all_columns_empty):
    instance = BaseVMC()
    columns, max_column = instance.pad_columns(all_columns_empty)
    assert max_column == 0
    for i in columns:
        assert(len(i)) == 0

def test_pad_last_column_empty(entries_0, last_column_empty_2):
    instance = BaseVMC()
    columns, max_column = instance.pad_columns(last_column_empty_2)
    assert max_column == 2
    for i in columns:
        assert(len(i)) == 2

def test_pad_lots_of_columns(entries_0, columns_many):
    instance = BaseVMC()
    columns, max_column = instance.pad_columns(columns_many(1000,5000))
    assert max_column == 1000
    for i in columns:
        assert(len(i)) == 1000

# Testing method build_rows
#   What to test
#   The method "build_rows" generates a set of rows that correspond vertically to the columns out of pad_columns
#   - number of rows corresponds to max_column value
#   - each row contains the number of elements specified by the setting NUMBER_OF_COLUMNS
#   - values in rows are the same as the corresponding cell in columns

def test_build_4(entries_0, padded_columns_4):
    instance = BaseVMC()
    instance.set_number_of_columns(num_cols = 4)
    original_columns = padded_columns_4
    num_rows = 4
    num_cols = 3
    
    rows = instance.build_rows(padded_columns_4, num_rows)

    assert len(rows) == num_rows  # number of rows corresponds to max_column value
    for row in rows:
        assert len(row) == num_cols  # each row contains the number of elements specified by the setting NUMBER_OF_COLUMNS

    reversed_columns = []
    for c in range(num_cols):
        col = [rows[r][c] for r in range(0, num_rows)]
        reversed_columns.append(col)
    assert reversed_columns == original_columns

def test_build_16(entries_0, padded_columns_16):
    instance = BaseVMC()  # only used to instantiate EvenBaseVMC
    instance.set_number_of_columns(num_cols = 3)
    original_columns = padded_columns_16
    num_rows = 16
    num_cols = 3

    rows = instance.build_rows(padded_columns_16, num_rows)

    assert len(rows) == num_rows  # number of rows corresponds to max_column value
    for row in rows:
        assert len(row) == num_cols
        # each row contains the number of elements specified by the setting NUMBER_OF_COLUMNS

    reversed_columns = []
    for c in range(num_cols):
        col = [rows[r][c] for r in range(0, num_rows)]
        reversed_columns.append(col)
    assert reversed_columns == original_columns



