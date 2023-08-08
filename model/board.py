from model.player import player

class board:
    EMPTY_SLOT = '0'
    def __init__(self,size:int=5) -> None:
        self.size = size
        self.player = player()
        self.board = [[[self.EMPTY_SLOT, self.EMPTY_SLOT] for j in range(self.size)] for i in range(self.player.lives)]
        pass

    def update_board(self,guess_graded:list):
        index = player.lives_start - player.lives_left #calcs index of which list affecting
        self.board[index] = guess_graded
        

    def __str__(self):
        return f"Size of Words/Board: {self.size}, Board: {self.board}"