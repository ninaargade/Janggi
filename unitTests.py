import unittest
import Janggi


class TestCase(unittest.TestCase):
    """TestCase class inherits from unittest.TestCase to form different methods as test cases. """

    def test_blueGuard(self):
        j = Janggi()
        result = j.make_move('d10', 'd9')
        self.assertTrue(result)

    def test2(self):
        pass

if __name__ == '__main__':
    unittest.main()
