import unittest
from program import calculator

class TestCase(unittest.TestCase):
    
	def test_1(self):
		self.assertEqual(calculator().addition(4, 5), 9)
		
	def test_2(self):
		self.assertEqual(calculator().subtract(8, 3), 5)

	def test_3(self):
		self.assertEqual(calculator().multiply(2, 4), 8)

	def test_4(self):
		self.assertEqual(calculator().divide(9, 3), 3)

if __name__ == '__main__':
	unittest.main()