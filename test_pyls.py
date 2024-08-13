import pytest
from pyls import list_files

def test_list_files():
    files = list_files()
    assert isinstance(files, list)
    assert len(files) > 0
