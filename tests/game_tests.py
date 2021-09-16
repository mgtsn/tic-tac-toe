import unittest

from context import game


class TestGameStart(unittest.TestCase):
    def setUp(self):
        self.game = game.Game()


if __name__ == "__main__":
    unittest.main()
