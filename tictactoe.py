import enum
import random
from pprint import pprint

class Player(enum.Enum):
    x = 'x'
    o = 'o'


class IllegalMove(Exception):
    pass


class TicTacToe:
    def __init__(self):
        self.board = [
            ['blank', 'blank', 'blank'],
            ['blank', 'blank', 'blank'],
            ['blank', 'blank', 'blank']
        ]
        r = random.randint(0, 1)
        if r == 0:
            self.player = Player('x')
        else:
            self.player = Player('o')
        self.turn = 0

    def move(self, x, y):
        state = self.board[x][y]
        if state!= 'blank':
            raise IllegalMove("Cannot make that move - that position is already taken!")
        # Make the move
        self.board[x][y] = self.player.value

    def win(self):
        pprint("Player {} wins! Board: {}".format(self.player.value, str(self.board)))
        exit(0)

    def is_win(self):
        # rows
        # pprint("checking rows")
        for a_row in self.board:
            if len(set(a_row))==1 and 'blank' not in set(a_row):
                self.win()
        # pprint("checking cols")
        for column_index in range(0, 3):
            a_column = [self.board[0][column_index], self.board[2][column_index], self.board[2][column_index]]
            if len(set(a_column))==1 and 'blank' not in set(a_column):
                pprint("{} column win".format(column_index))
                self.win()
        r_diagonal = [self.board[i][i] for i in range(0, 3)]
        if len(set(r_diagonal)) == 1 and 'blank' not in set(r_diagonal):
            pprint("r diag win: {}".format(r_diagonal))
            self.win()
        l_diagonal = [self.board[0][2], self.board[1][1],self.board[2][0]]
        if len(set(l_diagonal)) == 1 and 'blank' not in set(l_diagonal):
            pprint("l diag win: {}".format(l_diagonal))
            self.win()
    def play(self):
        while self.turn <9:
            x, y = input("The board is currently {}.\n It's {}'s turn to move. \nEnter your move as x,y coordinates.\n".format(str(self.board), self.player.value)).split(',')
            try:
                self.move(int(x), int(y))
            except (IllegalMove, IndexError,ValueError):
                pprint("Illegal move! Try again")
                self.play()
            self.is_win()
            self.turn += 1

            # Next player's turn
            if self.player.value == 'x':
                self.player = Player.o
            else:
                self.player = Player.x

        print("It's a Draw!", str(self.board))

if __name__ == '__main__':
    game = TicTacToe()
    game.play()
