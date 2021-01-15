from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import ListView


class BaseVMC:
    """
    This is the base class for the specific VMC view classes. It contains common logic.
    """

    def set_number_of_columns(self, **kwargs):
        self.number_of_columns = kwargs.get("num_columns")
        if self.number_of_columns == None:
            _user_settings = getattr(settings, "VERTICAL_MULTI_COLUMNS", {})
            if _user_settings == {}:
                self.number_of_columns = 3
            else:
                self.number_of_columns = _user_settings["NUMBER_OF_COLUMNS"]

    def pad_columns(self, columns: list) -> [list, int]:
        # Determine the longest column so the rest can be padded to the same length
        max_column = max(len(i) for i in columns)
        # Pad shorter columns to the length of the longest
        for c in columns:
            for n in range(len(c), max_column):
                c.append("")
        return columns, max_column

    def build_rows(self, columns: list, num_rows: int) -> list:
        # Build the row lists to be passed to the template. The template must accommodate the same number of columns
        # as specified in settings or passed to the configuration.py function. (This defaults to 3 if not provided.)
        rows = []
        for r in range(0, num_rows):
            row = [columns[c][r] for c in range(0, self.number_of_columns)]
            rows.append(row)
        return rows


class EvenVMCView(BaseVMC, ListView):
    """
    Items are displayed vertically in the sorted order received. They are then rendered, spread as evenly as possible
    across the number of columns specified.
    """

    def __init__(self, **kwargs: int):
        self.set_number_of_columns(**kwargs)

    def get_data(self) -> list:
        """
        Override this method to retrieve data.
        Return a list of items in json format, sorted in the order you wish them displayed.
        """
        pass

    def process_entries(self, entries: list) -> list:
        number_of_entries = len(entries)
        entries_all = (
            number_of_entries // self.number_of_columns
        )  # minimum number of entries in all rows
        entries_some = (
            number_of_entries % self.number_of_columns
        )  # number of additional entries in some rows

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
                columns[col].append(entries[i])
            entries_pos += col_count[col]

        columns, max_column = self.pad_columns(columns)
        rows = self.build_rows(columns, max_column)
        return rows

    def get_queryset(self) -> list:
        entries = self.get_data()
        processed_entries = self.process_entries(entries)
        return processed_entries


class CriteriaVMCView(BaseVMC, ListView):
    """
    Items are displayed vertically in the order received. They are assigned to a column based on
    functions passed to the class, one function per column.
    """

    def __init__(self, **kwargs: int):
        self.set_number_of_columns(**kwargs)

    def get_data(self) -> list:
        """
        Override this method to retrieve data.
        Return a list of items in json format, sorted in the order you wish them displayed.
        """
        return []

    def get_column_criteria(self) -> list:
        """
        Override this method to retrieve the functions and keys needed to place data in the correct column.
        """
        return [[], []]

    def check_criteria(self, functions, keys):
        if not functions:
            raise ImproperlyConfigured(
                "Vertical-Multi-Columns/CriteriaVMCView-You have provided no list of functions defining column criteria."
            )
        elif len(functions) != self.number_of_columns:
            raise ImproperlyConfigured(
                "Vertical-Multi-Columns/CriteriaVMCView-The number of functions passed must correspond to the number of columns."
            )
        elif not keys:
            raise ImproperlyConfigured(
                "Vertical-Multi-Columns/CriteriaVMCView-You have not provided the keys to check in the column criteria functions)"
            )
        return

    def process_entries(self, entries: list, functions: list, keys: list) -> list:
        self.check_criteria(functions, keys)

        # create column lists using criteria functions passed in
        columns = [[] for c in range(self.number_of_columns)]
        for e in entries:
            for f in range(0, len(functions)):
                func = functions[f]
                parm = ""
                for k in keys:
                    if isinstance(e[k], int):
                        e[k] = str(e[k])
                    parm += e[k] + ","
                parm = parm[:-1]
                if func(parm):
                    columns[f].append(e)

        columns, max_column = self.pad_columns(columns)
        rows = self.build_rows(columns, max_column)
        return rows

    def get_queryset(self) -> list:
        entries = self.get_data()
        functions, keys = self.get_column_criteria()
        self.check_criteria(functions, keys)
        processed_entries = self.process_entries(entries, functions, keys)
        return processed_entries


class DefinedVMCView(BaseVMC, ListView):
    """
    Items are passed in defined columns and displayed as vertically in the same sorted order as received.
    Each column's contents are displayed without change.
    """

    def __init__(self, **kwargs: int):
        self.set_number_of_columns(**kwargs)

    def get_data(self):
        """
        Override this method to retrieve data (which in this case is a list of columns
        in json format that contain the sorted data you wish to display.
        """
        pass

    def check_columns(self, columns):
        if not columns:
            raise ImproperlyConfigured(
                "Vertical-Multi-Columns/DefinedVMCView-You have passed no columns."
            )
        elif len(columns) != self.number_of_columns:
            raise ImproperlyConfigured(
                "Vertical-Multi-Columns/DefinedVMCView-The number of columns passed must correspond to the number of columns."
            )

    def process_columns(self, columns) -> list:
        self.check_columns(columns)
        columns, max_column = self.pad_columns(columns)
        rows = self.build_rows(columns, max_column)
        return rows

    def get_queryset(self) -> list:
        columns = self.get_data()
        processed_entries = self.process_columns(columns)
        return processed_entries
