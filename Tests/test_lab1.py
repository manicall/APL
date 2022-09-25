import unittest
import lab1

class TestLab1(unittest.TestCase):
    def setUp(self):
        self.t16 = lab1.Task16()
        self.t21 = lab1.Task21()
        
    def test_area(self):
        self.assertEqual(round(self.t16.round_area(5), 1), 78.5)
