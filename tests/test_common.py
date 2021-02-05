import pytest
from vertical_multi_columns.views import _BaseVMC

# Testing method pad_columns
#   What to test
#   The method "pad_columns" generates columns equal in length to the longest column
#   - all columns already equal
#   - all columns empty
#   - first column empty
#   - last column empty
#   - lots of columns


def test_pad_columns_already_same(entries_0, columns_same_length_4):
    instance = _BaseVMC()
    columns, max_column = instance.pad_columns(columns_same_length_4)
    assert max_column == 4
    for i in columns:
        assert (len(i)) == 4


def test_pad_first_column_empty(entries_0, first_column_empty_5):
    instance = _BaseVMC()
    columns, max_column = instance.pad_columns(first_column_empty_5)
    assert max_column == 5
    for i in columns:
        assert (len(i)) == 5


def test_pad_all_columns_empty(entries_0, all_columns_empty):
    instance = _BaseVMC()
    columns, max_column = instance.pad_columns(all_columns_empty)
    assert max_column == 0
    for i in columns:
        assert (len(i)) == 0


def test_pad_last_column_empty(entries_0, last_column_empty_2):
    instance = _BaseVMC()
    columns, max_column = instance.pad_columns(last_column_empty_2)
    assert max_column == 2
    for i in columns:
        assert (len(i)) == 2


def test_pad_lots_of_columns(entries_0, columns_many):
    instance = _BaseVMC()
    columns, max_column = instance.pad_columns(columns_many(1000, 5000))
    assert max_column == 1000
    for i in columns:
        assert (len(i)) == 1000


# Testing method build_new_rows
#   What to test
#   The method "build_new_rows" generates a set of rows that correspond vertically to the passed columns
#   - number of rows corresponds to max_column value
#   - each row contains the number of elements specified by the setting NUMBER_OF_COLUMNS
#   - values in rows are the same as the corresponding cell in columns

# The next two tests are verifying the same thing.
# I've included them for my own documentation.
# They demonstrate using a parametrized fixture versus passing multiple fixtures with getfixturevalue()


def test_build_using_parametrized_fixture(padded_columns):
    original_columns = padded_columns[0]
    out_column_length = padded_columns[1]
    num_cols = padded_columns[2]
    instance = _BaseVMC(num_cols=num_cols)
    rows = instance.build_new_rows(original_columns, out_column_length)

    assert (
        len(rows) == out_column_length
    )  # number of rows corresponds to max length of the original columns
    for row in rows:
        assert (
            len(row) == instance.number_of_columns
        )  # each row contains the number of elements specified by the setting NUMBER_OF_COLUMNS

    reversed_columns = []
    for c in range(instance.number_of_columns):
        col = [rows[r][c] for r in range(out_column_length)]
        reversed_columns.append(col)
    assert (
        reversed_columns == original_columns
    )  # when "unbuilt" the result should be identical to the original columns


@pytest.mark.parametrize(
    "padded_columns", [("fixture_padded_columns_4"), ("fixture_padded_columns_16")]
)
def test_build_using_getfixturevalue(padded_columns, request):
    padded_columns = request.getfixturevalue(padded_columns)
    original_columns = padded_columns[0]
    out_column_length = padded_columns[1]
    num_cols = padded_columns[2]
    instance = _BaseVMC(num_cols=num_cols)
    rows = instance.build_new_rows(original_columns, out_column_length)

    assert (
        len(rows) == out_column_length
    )  # number of rows corresponds to max length of the original columns
    for row in rows:
        assert (
            len(row) == instance.number_of_columns
        )  # each row contains the number of elements specified by the setting NUMBER_OF_COLUMNS

    reversed_columns = []
    for c in range(instance.number_of_columns):
        col = [rows[r][c] for r in range(out_column_length)]
        reversed_columns.append(col)
    assert (
        reversed_columns == original_columns
    )  # when "unbuilt" the result should be identical to the original columns
