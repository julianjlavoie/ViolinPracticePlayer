import unittest
from welcome import welcome

class test_welcome(unittest.TestCase):
    def testGavot(self):
        self.assertEqual(welcome())

