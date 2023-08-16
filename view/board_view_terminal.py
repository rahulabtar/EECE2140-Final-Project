from model.board import board
from view.board_view import BoardView

class BoardViewConsole(BoardView):
  """This class is a child class of the BoardView class. It represents a BoardView in the Console
  """
  def __init__(self, board: board) -> None:
    """This method initializes an instance of the BoardViewConsole class

    Args:
        board (board): A instance of the board class from the model
    """
    super().__init__(board)

  def display(self):
    """This method displays the board in the console with the board data by referencing the board class, the player class, and the print function
    """
    print('! represents a letter that is in the word you are guressing but incorrect spot')
    print('* represents a letter that is also in the word you are trying to guess AND is in the correct spot')
    rounds = self.board.player.lives_start
    size = self.board.size
    for i in range(rounds):
      print('____'*size)
      print()
      for j in range(size):
        print(self.board.board[i][j][0],end='   ')
      print()
      for j in range(size):
        print(self.board.board[i][j][1],end='   ')
      print()
    print('____'*size)

