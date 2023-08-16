from abc import ABC, abstractmethod
from model.board import board

#This class serves as the base class for all future board view classes
#in order to be considered a board view, other views must be child classes of this class
#and therefore have at least this classes certain methods

class BoardView(ABC):
  """The base class for all the board views. Board view is in charge of displaying the grid of the board
  and the words the player has guessed only
  """
  def __init__(self, board: board) -> None:
    """This method initializes the boardview abstract class with an instance of the board class

    Args:
        board (board): An instance of the board class, initalized elsewhere
    """
    self.board = board

  @abstractmethod
  def display(self):
    """A method that displays the board. 
    """
    pass