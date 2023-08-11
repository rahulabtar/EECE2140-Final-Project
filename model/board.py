from model.player import player

class board:
    EMPTY_SLOT = ' '
    def __init__(self,player: player,size:int=5) -> None:
        self.size = size
        self.player = player
        self.board = [[[self.EMPTY_SLOT, self.EMPTY_SLOT] for j in range(self.size)] for i in range(self.player.lives_start)]
        pass

    def update_board(self,guess_graded:list):
        index = self.player.lives_start - int(self.player.get_lives_left()) #calcs index of which list affecting
        #print("Lives started with", self.player.lives_start,"Lives left", self.player.lives_left,'Index', index)
        self.board[index] = guess_graded
        

    def __str__(self):

        return f"Size of Words/Board: {self.size}, Board: {self.board}"
    def clear_board(self):
        self.board = [[[self.EMPTY_SLOT, self.EMPTY_SLOT] for j in range(self.size)] for i in range(self.player.lives_start)]
