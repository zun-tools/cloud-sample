import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from calc import add, average


def test_add():
    assert add(1, 2) == 3


def test_average():
    assert average([1, 2]) == 1.5
