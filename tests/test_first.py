import pytest
import sys
from main import *
sys.path.insert(0, '../galact')


def inc(x):
    return x + 1


maini()


def test_answer():
    assert inc(4) == 5
