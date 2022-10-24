class EVAGoSimulation:
    board: list
    _PLAYER_BLACK = " 0 "
    _PLAYER_WHITE = " 1 "
    _black_move_done = False
    _white_move_done = False

    def __init__(self, board):
        self.board = board

    def display_board(self, board):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                print(board[i][j], end='')
            print()

    def black_move(self):
        i, j = input("Black to move: ").split()
        if self.board[int(i)][int(j)] == ' * ':
            if self.board[int(i)][int(j)] != self._PLAYER_BLACK or self.board[int(i)][int(j)] != self._PLAYER_WHITE:
                self.board[int(i)][int(j)] = self._PLAYER_BLACK
                self.display_board(self.board)
                self._black_move_done = True

        if self.board[int(i)][int(j)] == self._PLAYER_BLACK:
            self.board[int(i)][int(j)] = self._PLAYER_BLACK
            self.display_board(self.board)
            self._black_move_done = False
        elif self.board[int(i)][int(j)] == self._PLAYER_WHITE:
            self.board[int(i)][int(j)] = self._PLAYER_WHITE
            self.display_board(self.board)
            self._black_move_done = False
        else:
            self.board[int(i)][int(j)] = ' * '
            self.display_board(self.board)
            self._black_move_done = False

    def white_move(self):
        i, j = input("White to move: ").split()
        if self.board[int(i)][int(j)] == ' * ':
            if self.board[int(i)][int(j)] != self._PLAYER_BLACK or self.board[int(i)][int(j)] != self._PLAYER_WHITE:
                self.board[int(i)][int(j)] = self._PLAYER_WHITE
                self.display_board(self.board)
                self._white_move_done = True

        if self.board[int(i)][int(j)] == self._PLAYER_BLACK:
            self.board[int(i)][int(j)] = self._PLAYER_BLACK
            self.display_board(self.board)
            self._black_move_done = False
        elif self.board[int(i)][int(j)] == self._PLAYER_WHITE:
            self.board[int(i)][int(j)] = self._PLAYER_WHITE
            self.display_board(self.board)
            self._black_move_done = False
        else:
            self.board[int(i)][int(j)] = ' * '
            self.display_board(self.board)
            self._black_move_done = False

    def play(self):
        while True:
            if not self._black_move_done:
                self.black_move()
                self._black_move_done = False
            self.white_move()
            self._white_move_done = False


board = [
    [
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * '
    ],
    [
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * '
    ],
    [
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * '
    ],
    [
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * '
    ],
    [
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * '
    ],
    [
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * '
    ],
    [
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * '
    ],
    [
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * '
    ],
    [
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * '
    ],
    [
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * '
    ],
    [
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * '
    ],
    [
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * '
    ],
    [
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * '
    ],
    [
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * '
    ],
    [
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * '
    ],
    [
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * '
    ],
    [
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * '
    ],
    [
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * '
    ],
    [
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * ', ' * ', ' * ',
        ' * '
    ]
]

sim = EVAGoSimulation(board)
sim.display_board(sim.board)
sim.play()