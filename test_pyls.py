import pytest
from pyls import list_files_with_details

def test_list_files_with_details():
    files = list_files_with_details()
    assert isinstance(files, list)
    assert len(files) > 0
    for file in files:
        details = file.split()
        assert len(details) == 3
        assert len(details[0]) == 19  # Date and time length
        assert details[1].isdigit()  # Size should be a digit
