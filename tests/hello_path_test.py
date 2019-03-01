import pytest
import os
from pathing.printpath import Pathing

p = Pathing()

def test_path_from_printpath_to_testcsv():
    assert p.get_test_file() == 'hello?'
