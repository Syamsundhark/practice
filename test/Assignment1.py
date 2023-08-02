import unittest
from src.Assignment1 import util

def ultramain(num):
    a=[]
    a.insert(0,5)
    a.insert(1,10)
    a.insert(0,6)
    print(a)
    a.remove(6)
    a.append(9)
    a.append(1)
    a.sort()
    print(a)
    a.pop()
    a.reverse()
    print(a)

class MyTestCase(unittest.TestCase):
    def test_something(self):
        input=12
#         output=[6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]
        self.assertEqual(util.main(12), ultramain(input))  # add assertion here


if __name__ == '__main__':
    unittest.main()
