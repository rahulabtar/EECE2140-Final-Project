from model.board import board
from view.board_view import BoardView

class BoardViewConsole(BoardView):
  def __init__(self, board: board) -> None:
    super().__init__(board)

  def display(self):
    print('! represents a letter that is in the word you are guressing but incorrect spot')
    print('* represents a letter that is also in the word you are trying to guess AND is in the correct spot')
    print('__'*board.size)