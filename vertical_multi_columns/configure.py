from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

class Distribution:
    '''
    This is the base class for the specific distribution classes. It contains their common logic.
    '''
    def __init__(self, **kwargs):
        self.number_of_columns = kwargs.get('num_columns')
        if self.number_of_columns == None:
            _user_settings = getattr(settings, 'VERTICAL_MULTI_COLUMNS', {})
            if _user_settings == {}:
                self.number_of_columns = 3
            else:
                self.number_of_columns = _user_settings['NUMBER_OF_COLUMNS']

    def pad_columns(self, columns: list) -> [list,int]:
        # Determine the longest column so the rest can be padded to the same length
        max_column = max(len(i) for i in columns)
        # Pad shorter columns to the length of the longest
        for c in columns:
            for n in range(len(c), max_column):
                c.append('')
        return columns, max_column

    def build_rows(self, columns: list, num_rows: int) -> list:
        # Build the row lists to be passed to the template. The template must accommodate the same number of columns
        # as specified in settings or passed to the configuration.py function. (This defaults to 3 if not provided.)
        rows = []
        for r in range(0, num_rows):
            row = [columns[c][r] for c in range(0, self.number_of_columns)]
            rows.append(row)
        return rows

class EvenDistribution(Distribution):
    '''
    Items are displayed vertically in the sorted order received. They are then spread as evenly as possible
    across the number of columns specified.
    '''

    def __init__(self, entries: list, **kwargs: int):
        super().__init__(**kwargs)
        self.entries = entries
        self.number_of_entries = len(self.entries)        

    def process(self) -> list:
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
    '''
    Items are displayed vertically in the sorted order received. They are assigned to a column based on
    functions passed to the class, one function per column.   
    '''
    
    def __init__(self, entries: list, column_criteria: list, func_args: list, **kwargs: int):
        super().__init__(**kwargs)
        self.entries = entries
        self.number_of_entries = len(self.entries)
        self.column_criteria = column_criteria
        self.func_args = func_args

    def check_criteria(self):
        if not self.column_criteria:
            raise ImproperlyConfigured(
                "Vertical-Multi-Columns/CriteriaDistribution-You have provided no list of functions defining column criteria.")
        elif len(self.column_criteria) != self.number_of_columns:
            raise ImproperlyConfigured(
                "Vertical-Multi-Columns/CriteriaDistribution-The number of functions passed must correspond to the number of columns.")
        elif not self.func_args:
            raise ImproperlyConfigured(
                "Vertical-Multi-Columns/CriteriaDistribution-You have not provided any fields to check for the column criteria functions)")
        return

    def process(self) -> list:
        self.check_criteria()
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
        
class DefinedDistribution(Distribution):
    '''
    Items are passed in defined columns and displayed as vertically in the same sorted order as received.
    Each column's contents are displayed without change.   
    '''

    def __init__(self, columns: list, **kwargs: int):
        super().__init__(**kwargs)
        self.columns = columns
        
    def check_columns(self):
        if not self.columns:
            raise ImproperlyConfigured(
            "Vertical-Multi-Columns/DefinedDistribution-You have passed no columns.")
        elif len(self.columns) != self.number_of_columns:
            raise ImproperlyConfigured(
                "Vertical-Multi-Columns/DefinedDistribution-The number of columns passed must correspond to the number of columns specified.")
                
    def process(self) -> list:
        self.check_columns()
        columns, max_column = self.pad_columns(self.columns)
        rows = self.build_rows(columns, max_column)
        return rows