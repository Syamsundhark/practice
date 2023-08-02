import unittest
from src.Assignment6 import util
def new_values(number):
    for i in range(1,number+1):
        hex_des="{0:x}".format(i)
        print(i," ",oct(i)[2:]," ",hex_des," ",bin(i)[2:])

class MyTestCase(unittest.TestCase):
    def test_something(self):
        number=17
        a=util.values(number)
        r=new_values(number)
        self.assertEqual(a,r)  # add assertion here


if __name__ == '__main__':
    unittest.main()
