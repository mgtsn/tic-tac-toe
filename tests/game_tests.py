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
        self.assertFalse(self.game._board_full())


class TestGameWon(unittest.TestCase):
    def setUp(self):
        self.game = game.Game(3)

    def testEmpty(self):
        self.assertFalse(self.game.finished())

    def testWin(self):
        self.game.board[0] = ["X", "X", "X"]
        self.assertEqual(self.game.finished(), "X")

        self.game.board[0][0] = "O"
        self.game.board[1][0] = "O"
        self.game.board[2][0] = "O"
        self.assertEqual(self.game.finished(), "O")

    def testTie(self):
        self.game.board[0] = ["X", "O", "X"]
        self.game.board[1] = ["X", "O", "X"]
        self.game.board[2] = ["O", "X", "O"]
        self.assertEqual(self.game.finished(), "Tie")

    def testWinDiagonal(self):
        self.game.board[0] = ["O", "O", "X"]
        self.game.board[1] = ["X", "O", "X"]
        self.game.board[2] = ["O", "X", "O"]
        self.assertEqual(self.game.finished(), "O")

        self.game.board[2][0] = "X"
        self.game.board[1][1] = "X"
        self.assertEqual(self.game.finished(), "X")


if __name__ == "__main__":
    unittest.main()
