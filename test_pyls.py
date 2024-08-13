import pytest
from pyls import list_files, list_files_with_suffixes, list_files_with_details, list_files_with_details_and_suffixes, print_help

def test_list_files():
    files = list_files()
    assert isinstance(files, list)
    assert len(files) > 0

def test_list_files_with_suffixes():
    files = list_files_with_suffixes()
    assert isinstance(files, list)
    assert len(files) > 0
    for file in files:
        if file.endswith('/'):
            assert os.path.isdir(file[:-1])
        elif file.endswith('*'):
            assert os.access(file[:-1], os.X_OK)

def test_list_files_with_details():
    files = list_files_with_details()
    assert isinstance(files, list)
    assert len(files) > 0
    for file in files:
        details = file.split()
        assert len(details) == 3
        assert len(details[0]) == 19  # Date and time length
        assert details[1].isdigit()  # Size should be a digit

def test_list_files_with_details_and_suffixes():
    files = list_files_with_details_and_suffixes()
    assert isinstance(files, list)
    assert len(files) > 0
    for file in files:
        details = file.split()
        assert len(details) == 3
        assert len(details[0]) == 19  # Date and time length
        assert details[1].isdigit()  # Size should be a digit
        assert details[2].endswith(('/', '*', ''))  # Suffix check

def test_print_help(capfd):
    print_help()
    out, _ = capfd.readouterr()
    assert "pyls - A limited version of the ls command" in out
    assert "-F" in out
    assert "-l" in out
    assert "-h, --help" in out
