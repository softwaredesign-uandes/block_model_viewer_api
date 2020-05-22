from generate_blocks import generate_blocks
import unittest

class GenerateBlocksTest(unittest.TestCase):
  def test_generate_blocks_generates_expected_number_of_blocks(self):
    x_size = 5
    y_size = 3
    z_size = 3
    self.assertEqual(len(generate_blocks(x_size, y_size, z_size)), x_size * y_size * z_size)

  def test_generate_one_block_indices_are_zero(self):
    self.assertEqual(generate_blocks(1, 1, 1)[0]["x"], 0)
    self.assertEqual(generate_blocks(1, 1, 1)[0]["y"], 0)
    self.assertEqual(generate_blocks(1, 1, 1)[0]["z"], 0)

  def test_generate_one_block_grades_are_zero(self):
    self.assertEqual(generate_blocks(1, 1, 1)[0]["au"], 0.0)

    self.assertEqual(generate_blocks(1, 1, 1)[0]["cu"], 0.0)