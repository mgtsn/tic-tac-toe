import unittest

from context import game


class TestGameStart(unittest.TestCase):
    def setUp(self):
        self.game = game.Game(3)

    def testSize(self):
        self.assertEqual(self.game.size, 3)

    def testBoard(self):
        self.assertEqual(len(self.game.board), 3)
        for row in self.game.board:
            self.assertEqual(len(row), 3)
            for col in row:
                self.assertEqual(col, 0)


class TestGameMethods(unittest.TestCase):
    def setUp(self):
        self.game = game.Game(3)

    def testFull(self):
        self.assertFalse(self.game.board_full())


if __name__ == "__main__":
    unittest.main()
