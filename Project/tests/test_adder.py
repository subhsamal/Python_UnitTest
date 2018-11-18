# This is test_adder.py file
from proj.adder import adder
import unittest
import pytest


# class TestAdder(unittest.TestCase):
#    def test_simple(self):
#        res = adder(2,3)
#        self.assertEqual(res, 5)

def test_add():
    res = adder(2, 3)
    assert res == 5, "Value should be 5"

if __name__ == '__main__':
    unittest.main()
