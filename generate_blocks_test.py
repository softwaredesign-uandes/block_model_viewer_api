from generate_blocks import generate_blocks
import unittest

class GenerateBlocksTest(unittest.TestCase):
  def test_generate_blocks_generates_expected_number_of_blocks(self):
    x_size = 5
    y_size = 3
    z_size = 3
    self.assertEqual(len(generate_blocks(x_size, y_size, z_size)), x_size * y_size * z_size)