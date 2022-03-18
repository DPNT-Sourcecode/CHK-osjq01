import unittest
import SUM

class Testing(unittest.TestCase):
    def test_compute(self):
        a=5
        b=SUM.compute(2,3)
        self.assertEqual(a, b)