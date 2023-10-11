import unittest
import numpy as np
from matrix import LinearMxMultiply, DncMxMultiply, StrassenMxMultiply, PadMatrices

class MaxTest(unittest.TestCase):
  def setUp(self):
    self.testValues = []
    for i in range(32):
      rows = np.random.randint(1, 64)
      cols_a = np.random.randint(1, 64)
      cols_b = np.random.randint(1, 64)
      a = np.random.randint(-9, 9, (rows, cols_a))
      b = np.random.randint(-9, 9, (cols_a, cols_b))
      self.testValues.append((a, b))

  def test_linearMatrixMultiplication(self):
    self.matrixMultiplication(LinearMxMultiply)

  def test_DNCMatrixMultiplication(self):
    self.matrixMultiplication(DncMxMultiply)

  def test_strassenMatrixMultiplication(self):
    self.matrixMultiplication(StrassenMxMultiply)

  def test_matrix_padding(self):
    a = np.random.randint(-9, 9, (16, 16))
    b = np.random.randint(-9, 9, (16, 7))
    new_a, new_b = PadMatrices(a, b)
    self.assertSequenceEqual(new_a.shape, (16, 16))
    self.assertSequenceEqual(new_b.shape, (16, 16))


  def matrixMultiplication(self, f):
    for a, b in self.testValues:
      expected = np.matmul(a, b)
      actual = f(a, b)
      self.assertSequenceEqual(np.shape(expected), np.shape(actual))
      for i in range(len(actual)):
        self.assertListEqual(expected[i].tolist(), actual[i].tolist())
      
    

if __name__ == '__main__':
  unittest.main()