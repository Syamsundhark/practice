import unittest
from src.Assignment3 import util

class MyTestCase(unittest.TestCase):
    def test_something(self):
        n=2
        marks={"abc":[10,20,30],"bcd":[20,30,40]}
        qname="bcd"
        output=30
        z=util.avg(n,marks,qname)
        self.assertEqual(z,output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
