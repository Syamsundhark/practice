import unittest
from src.Assignment10 import util


class MyTestCase(unittest.TestCase):
    def test_something(self):
        l="a b c"
        output=0.6667
        self.assertEqual(util.prob(3,l, 2), output)  # add assertion here


if __name__ == '__main__':
    unittest.main()