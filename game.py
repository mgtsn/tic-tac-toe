class Game:
    def build_board(self, size):
        board = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(0)
            board.append(row)
        return board

    def __init__(self, size):
        self.size = size
        self.board = self.build_board(size)

    def _check_column(self, j):
        letter = self.board[0][j]
        if not letter:
            return
        for i in range(1, self.size):
            if self.board[i][j] != letter:
                return
        return letter

    def _check_row(self, i):
        letter = self.board[i][0]
        if not letter:
            return
        for j in range(1, self.size):
            if self.board[i][j] != letter:
                return
        return letter

    def _game_won(self):
        for i in range(self.size):
            r = self._check_row(i)
            if r:
                return r
            c = self._check_column(i)
            if c:
                return c
        return

    def _board_full(self):
        for row in self.board:
            for col in row:
                if not col:
                    return False
            return True

    def finished(self):
        if self._game_won():
            return self._game_won()
        elif self._board_full():
            return "Tie"
        return
