import unittest
from Janggi import JanggiGame


class TestCase(unittest.TestCase):
    """TestCase class inherits from unittest.TestCase to form different methods as test cases. """

    def test_blueGuard(self):
        j = JanggiGame()
        result = j.make_move('d10', 'd9')
        self.assertTrue(result)

    def test_redGuard(self):
        j = JanggiGame()
        result = j.make_move('d1', 'd2')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
