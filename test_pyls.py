import pytest
from pyls import print_help

def test_print_help(capfd):
    print_help()
    out, _ = capfd.readouterr()
    assert "pyls - A limited version of the ls"
