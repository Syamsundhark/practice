import unittest
from src.Assignment4 import util

class MyTestCase(unittest.TestCase):
    def test_something(self):
               a =util.mutate_string('abracadabra',5,'k')
               result='abrackdabra'

               self.assertEqual(a,result)


if __name__ == '__main__':
    unittest.main()
