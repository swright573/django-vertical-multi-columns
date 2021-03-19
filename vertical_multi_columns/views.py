""" Django Vertical Multi Columns Generator

Classes:
    EvenVMCView
    CriteriaVMCView
    DefinedVMCView
    _BaseVMC
"""

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import ListView

MSGSTART = "Vertical-Multi-Columns/CriteriaVMCView-"


class _BaseVMC:
    """
    This is the base class for the specific VMC view classes. It contains common logic.
    """

    @classmethod
    def get_number_of_columns(cls, **kwargs: int):
        """Determine the number of columns to be generated"""
        number_of_columns = kwargs.get("num_columns")
        if number_of_columns is None:
            try:
                _user_settings = getattr(settings, "VERTICAL_MULTI_COLUMNS")
                number_of_columns = list(map(lambda x: x["NUMBER_OF_COLUMNS"], _user_settings))[0]
            except (AttributeError, TypeError):
                number_of_columns = 3
        return number_of_columns

    @classmethod
    def pad_columns(cls, columns: list) -> [list, int]:
        """Determines the longest column so the rest can be padded to the same length"""
        max_column = max(len(i) for i in columns)
        # Pad shorter columns to the length of the longest
        for column in columns:
            for _ in range(len(column), max_column):
                column.append("")
        return columns, max_column

    @classmethod
    def build_new_rows(cls, columns: list, num_rows: int) -> list:
        """Builds the rows list to be passed to the template which must accommodate the expected number of columns."""
        new_rows = []
        for row in range(num_rows):
            new_row = [columns[col][row] for col in range(len(columns))]
            new_rows.append(new_row)
        return new_rows


class EvenVMCView(_BaseVMC, ListView):
    """
    Items can be displayed vertically in side-by-side columns in the order received.
    Items are assigned to columns as evenly as possible.
    The number of columns can be specified in settings or passed to the class.

    Methods
    -------
    get_data():
        User will override to get the data to be displayed.
    process_entries():
        Generates the JSON-formatted list to be passed to the template.
    get_queryset():
        Overrides a ListView method, passing the response to the
        template.
    """

    def __init__(self, **kwargs: int):
        """Constructs the class. Optional kwarg 'num_columns' overrides any value in settings."""
        self.number_of_columns = self.get_number_of_columns(**kwargs)

    def get_data(self) -> list:
        """
        Override this method to retrieve data.
        Return a list of items in json format, sorted in the order you wish them displayed.
        """

    def process_entries(self, entries: list) -> list:
        """
        Morph the passed data into "rows" containing the same number of items
        as the number of columns requested. At the same time, keep the columns
        in the sort order passed.
        """
        if entries:
            number_of_entries = len(entries)
            entries_all = number_of_entries // self.number_of_columns  # minimum number of entries in all rows
            entries_some = number_of_entries % self.number_of_columns  # number of additional entries in some rows

            # Create column structure and calculate column lengths
            columns = [[] for i in range(self.number_of_columns)]
            col_count = [0 for i in range(self.number_of_columns)]
            for i in range(self.number_of_columns):
                col_count[i] = entries_all
                if entries_some > 0:
                    col_count[i] += 1
                    entries_some -= 1
            # Populate columns based on number of entries in each column
            entries_pos = 0
            for col in range(self.number_of_columns):
                for i in range(entries_pos, entries_pos + col_count[col]):
                    columns[col].append(entries[i])
                entries_pos += col_count[col]

            columns, max_column = self.pad_columns(columns)
            rows = self.build_new_rows(columns, max_column)
        else:
            rows = []
        return rows

    def get_queryset(self) -> list:
        """ Overridden ListView method to send the response object to the template."""

        entries = self.get_data()
        processed_entries = self.process_entries(entries)
        return processed_entries


class CriteriaVMCView(_BaseVMC, ListView):
    """
    Items can be displayed vertically in side-by-side columns.
    Each column remains in the sort order received.
    Items are assigned to columns based on criteria passed to the class.
    The number of columns can be specified in settings or passed to the class.

    Methods
    -------
    get_data():
        User will override to get the data to be displayed.
    get_column_criteria():
        User will override to pass the functions/keys to be used
        to place data in columns.
    check_criteria():
        Verifies criteria (functions/keys) have been passed and that
        the number of functions corresponds to the number of columns
        specified.
    process_entries():
        Generates the JSON-formatted list to be passed to the template.
    get_queryset():
        Overrides a ListView method, passing the response to the
        template.
    """

    def __init__(self, **kwargs: int):
        """Constructs the class. Optional kwarg 'num_columns' overrides any value in settings."""
        self.number_of_columns = self.get_number_of_columns(**kwargs)

    def get_data(self) -> list:
        """
        Override this method to retrieve data.
        Return a list of items in json format, sorted in the order you wish them displayed.
        """
        return []

    def get_column_criteria(self) -> list:
        """Override this method to retrieve the functions and keys used to place data in columns."""
        return [[], []]

    def check_criteria(self, functions, keys):
        """
        Verifies column criteria functions have been passed, there
        are the correct number, and keys that are referenced in the
        functions were passed.
        """

        if not functions:
            raise ImproperlyConfigured(MSGSTART + "You have provided no list of functions defining column criteria.")
        if len(functions) != self.number_of_columns:
            raise ImproperlyConfigured(
                MSGSTART + "Number of functions passed must correspond to number of columns in settings."
            )
        if not keys:
            raise ImproperlyConfigured(MSGSTART + "You must provide keys used in column criteria functions)")

    def process_entries(self, entries: list, functions: list, keys: list) -> list:
        """
        Check that there is data to display. If so, morph the passed data into "rows", placing data in columns using
        the passed functions/keys. At the same time, keep the columns in the sort order passed.
        """

        if entries:
            self.check_criteria(functions, keys)

            # create column lists using criteria functions passed in
            columns = [[] for c in range(self.number_of_columns)]
            for entry in entries:
                efunctions = enumerate(functions)
                for pos, func in efunctions:
                    parm = []
                    for key in keys:
                        parm.append(entry[key])
                    if func(parm):
                        columns[pos].append(entry)
            columns, max_column = self.pad_columns(columns)
            rows = self.build_new_rows(columns, max_column)
        else:
            rows = []
        return rows

    def get_queryset(self) -> list:
        """ Overridden ListView method to send the response object to the template."""

        entries = self.get_data()
        functions, keys = self.get_column_criteria()
        self.check_criteria(functions, keys)
        processed_entries = self.process_entries(entries, functions, keys)
        return processed_entries


class DefinedVMCView(_BaseVMC, ListView):
    """
    Items are passed in defined columns which can be displayed side-by-side in a template.
    Each column's contents are displayed without change.
    """

    def __init__(self, **kwargs: int):
        """Constructs the class. Optional kwarg 'num_columns' overrides any value in settings."""
        self.number_of_columns = self.get_number_of_columns(**kwargs)

    def get_data(self):
        """
        Override this method to retrieve data (which in this case is a list of columns
        in json format that contain the sorted data you wish to display.
        """

    def check_columns(self, columns):
        """
        Verifies the correct number of columns were passed.
        """

        if not columns:
            raise ImproperlyConfigured(MSGSTART + "You have passed no columns.")
        if len(columns) != self.number_of_columns:
            raise ImproperlyConfigured(
                MSGSTART + "The number of columns passed must correspond to the number of columns setting."
            )

    def process_columns(self, columns) -> list:
        """
        Morph the passed columns into "rows" containing the same number of items
        as the number of columns requested. At the same time, keep the columns
        in the sort order passed.
        """

        self.check_columns(columns)
        columns, max_column = self.pad_columns(columns)
        rows = self.build_new_rows(columns, max_column)
        return rows

    def get_queryset(self) -> list:
        """ Overridden ListView method to send the response object to the template."""

        columns = self.get_data()
        processed_entries = self.process_columns(columns)
        return processed_entries
