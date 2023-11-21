#!/usr/bin/python3
import unittest


class LearnTest(unittest.TestCase):
    """unittest class"""

    def test_funt_1(self):
        pass

    def test_funt_2(self):
        pass
    """if you write a function without
    starting with the word 'test',
    it will run as normal function
    as shown below"""
   # def funct(self):
       # pass
    """this will not run as test"""

   # def testfunct(self):
       # pass
    """this will run as test"""


if __name__ == "__main__":
    unittest.main()
