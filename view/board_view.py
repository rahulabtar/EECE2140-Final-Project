from abc import ABC, abstractmethod
from model.board import board

class BoardView(ABC):
  """The base class for all the board views
  """
  def __init__(self, board: board) -> None:
    self.board = board

  @abstractmethod
  def display(self):
    pass