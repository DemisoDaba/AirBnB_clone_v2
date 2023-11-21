#!/usr/bin/python3

"""write unittest using trple A model
means
Arrange = preriquisit to run the test
Act = run the test
Assert = verify the test """

import unittest

def sum(a, b):
    return a + b


class SumTest(unittest.TestCase):

    def setUp(self):
        """ for a universal change in the function"""
        print("SETUP CALL........")
        #Arrange
        self.a = 234
        self.b = 445

    def tearDown(self):
        print("TEAR DOWN CALL.....")

    def test_sum_fun1(self):
        print("Test 1 call.....")
        # Arrange
        # a = 123
        # b = 340

        # Act
        result = sum(self.a, self.b)

        #Assert
        self.assertEqual(result, self.a + self.b)

    def test_sum_fun2(self):
        print("Test 2 call.....")
        # Arrange
        # a = 123
        # b = 340

        # Act
        result = sum(self.b, self.a)

        #Assert
        self.assertEqual(result, self.a + self.b)



if __name__ == "__main__":
    unittest.main()
