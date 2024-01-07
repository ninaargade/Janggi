import unittest
from Janggi import JanggiGame


class TestCase(unittest.TestCase):
    """TestCase class inherits from unittest.TestCase to form different methods as test cases."""

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
        result = j.is_in_check("blue")
        self.assertFalse(result)

    def test_isInCheckmate_Blue(self):
        j = JanggiGame()
        result = j.is_in_checkmate_blue()
        self.assertFalse(result)

    def test_blueHorse_False(self):
        j = JanggiGame()
        result = j.make_move('c10', 'b8')
        self.assertFalse(result)

    def test_blueHorse_True(self):
        j = JanggiGame()
        result = j.make_move('c10', 'd8')
        self.assertTrue(result)

    def test_blueElephant(self):
        j = JanggiGame()
        result = j.make_move('b10', 'd7')
        self.assertTrue(result)

    def test_blueChariot(self):
        j = JanggiGame()
        result = j.make_move('a10', 'a8')
        self.assertTrue(result)
    
    def test_blueCannon(self):
        j = JanggiGame()
        result = j.make_move('b8', 'b1')
        self.assertTrue(result)

    def test_blueSoldier(self):
        pass
if __name__ == '__main__':
    unittest.main()
