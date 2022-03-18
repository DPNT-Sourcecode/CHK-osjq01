import unittest

class Testing(unittest.TestCase):
    def test_compute(self):
        a=5
        b=compute(2,3)
        self.assertEqual(a, b)