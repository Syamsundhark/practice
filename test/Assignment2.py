import unittest
from src.Assignment2 import util

class MyTestCase(unittest.TestCase):
    def test_something(self):
        score=[10,20,30,40]
        y=util.main(score)
        result=30
        self.assertEqual(y, result)  # add assertion here


if __name__ == '__main__':
    unittest.main()
