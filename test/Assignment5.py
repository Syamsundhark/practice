import unittest
from src.Assignment5 import util


def new_final(string, k):
    temp = []
    len_temp = 0
    for i in string:
        len_temp += 1
        if i not in temp:
            temp.append(i)
        if len_temp == k:
            res = ''.join(temp)
            temp = []
            len_temp = 0

class MyTestCase(unittest.TestCase):

    def test_something(self):
        a=util.final("AABCAAADA",3)
        string="AABCAAADA"
        k=3
        expected_output=new_final(string, k)
        self.assertEqual(a,expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()
