import unittest
from src.Assignment7 import util

class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr=[1,2,3,4,5]
        set1={2,3,4}
        set2={5,7}
        output=2
        self.assertEqual(util.happiness(arr,set1,set2), output)  # add assertion here


if __name__ == '__main__':
    unittest.main()

