from django.core.exceptions import ImproperlyConfigured
from django.conf import settings

class Distribution:

    def __init__(self, entries):
        self.entries = entries
        self.number_of_entries = len(self.entries)
        _user_settings = getattr(settings, 'VERTICAL_MULTI_COLUMNS', {})
        if _user_settings == {}:
            self.number_of_columns = 3
        else:
            self.number_of_columns = _user_settings['NUMBER_OF_COLUMNS']

    def pad_columns(self, columns):
        # Determine the longest column so the rest can be padded to the same length
        max_column = max(len(i) for i in columns)
        # Pad shorter columns to the length of the longest
        for c in columns:
            for n in range(len(c), max_column):
                c.append('')
        return columns, max_column

    def build_rows(self, columns, num_rows):
        # Build the row lists to be passed to the template. The template must accommodate the same number of columns
        # as specified in settings (which defaults to 3 if not provided).
        rows = []
        for r in range(0, num_rows):
            row = [columns[c][r] for c in range(0, self.number_of_columns)]
            rows.append(row)
        return rows

class EvenDistribution(Distribution):
    """
    Items are displayed vertically in the sorted order provided spread as evenly as possible
    across the number of columns specified in settings. This defaults to 3 if no number if provided.
    """

    def __init__(self, entries):
        super().__init__(entries)

    def process(self):
        entries_all = self.number_of_entries // self.number_of_columns    # minimum number of entries in all rows
        entries_some = self.number_of_entries % self.number_of_columns    # number of additional entries in some rows

        # Create columns and calculate column lengths
        columns = [[] for i in range(self.number_of_columns)]
        col_count = [0 for i in range(self.number_of_columns)]
        for i in range(self.number_of_columns):
            col_count[i] = entries_all
            if entries_some > 0:
                col_count[i] += 1
                entries_some -= 1

        # Create column lists based on number of entries in each column
        entries_pos = 0
        for col in range(self.number_of_columns):
            for i in range(entries_pos, entries_pos + col_count[col]):
                columns[col].append(self.entries[i])
            entries_pos += col_count[col]

        columns, max_column = self.pad_columns(columns)
        rows = self.build_rows(columns, max_column)
        return rows


class CriteriaDistribution(Distribution):

    def __init__(self, entries, column_criteria, func_args):
        super().__init__(entries)
        self.column_criteria = column_criteria
        self.func_args = func_args

    def criteria(self):
        if not self.column_criteria:
            raise ImproperlyConfigured(
                "Vertical-Multi-Columns-You have provided no list of functions defining column criteria.")
        elif len(self.column_criteria) != self.number_of_columns:
            raise ImproperlyConfigured(
                "Vertical-Multi-Columns-The number of functions passed must correspond to the number of columns.")
        elif not self.func_args:
            raise ImproperlyConfigured(
                "Vertical-Multi-Columns-You have not provided any fields to check for the column criteria functions)")
        return

    def process(self):
        self.criteria()
        # create column lists based on criteria passed in
        columns = [[] for i in range(self.number_of_columns)]
        for i in self.entries:
            for j in range(0, len(self.column_criteria)):
                func = self.column_criteria[j]
                parm = ''
                for x in self.func_args:
                    if isinstance(i[x], int):
                        i[x] = str(i[x])
                    parm += i[x] + ","
                parm = parm[:-1]
                if func(parm):
                    columns[j].append(i)

        columns, max_column = self.pad_columns(columns)
        rows = self.build_rows(columns, max_column)
        return rows
