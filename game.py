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

    def board_full(self):
        for row in self.board:
            for col in row:
                if not col:
                    return False
            return True
