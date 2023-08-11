from abc import ABC, abstractmethod
from view.board_view import BoardView
from model.player import player

class GameView(ABC):
  """This class represents the game view
  """
  def __init__(self, board_view: BoardView,player:player) -> None:
    self.board_view = board_view
    self.player = player

  @abstractmethod
  def display_lives(self, player: player):
    pass

  @abstractmethod
  def get_guess(self):
    pass

  @abstractmethod
  def display_invalid_guess(self):
    pass

  def display_board(self):
    self.board_view.display()

  @abstractmethod
  def display_win(self):
    pass

  @abstractmethod
  def display_loss(self):
    pass

  @abstractmethod
  def display_play_again(self):
    pass
  
  @abstractmethod
  def say_goodbye(self):
    pass