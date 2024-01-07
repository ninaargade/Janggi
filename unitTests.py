import unittest
from Janggi import JanggiGame


class TestCase(unittest.TestCase):
    """TestCase class inherits from unittest.TestCase to form different methods as test cases. """

    def test_blueGuard(self):
        j = JanggiGame()
        result = j.make_move('d10', 'd9')
        self.assertTrue(result)

    def test_getTurn(self):
        j = JanggiGame()
        result = j.get_turn()
        self.assertEqual(result, 'Blue')

    def test_getGameState(self):
        j = JanggiGame()
        result = j.get_game_state()
        self.assertEqual(result, 'UNFINISHED')

    def test_isInCheck(self):
        j = JanggiGame()
        result = j.is_in_check()
        self.assertFalse(result)

    def test_isInCheckmate_Blue(self):
        j = JanggiGame()
        result = j.is_in_checkmate_blue()
        self.assertFalse(result)
        
if __name__ == '__main__':
    unittest.main()
