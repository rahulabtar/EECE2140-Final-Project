from abc import ABC, abstractmethod
from view.board_view import BoardView
from model.player import player

class GameView(ABC): 
  """This class represents the game view. In order for any future views to be considered a game view, they must
  inherit from this class and therefore contain its given methods 
  """
  def __init__(self, board_view: BoardView,player:player) -> None:
    """This method initializes an instance of the GameView class with a instance of the BoardView class and 
    the given instance of the player class

    Args:
        board_view (BoardView): A instance of the BoardView class
        player (player): A instace of the player class
    """
    self.board_view = board_view
    self.player = player

  @abstractmethod
  def display_lives(self, player: player):
    """This method displays the amount of lives the player has left to the user

    Args:
        player (player): A instance of the player class
    """
    pass

  @abstractmethod
  def get_guess(self):
    """This method gets gets a guess from the user via statement or window
    """
    pass

  @abstractmethod
  def display_invalid_guess(self):
    """This method displays an error statement if the player's guess in invalid
    """
    pass

  def display_board(self):
    """This method displays the board by calling the corresponding boardview method
    """
    self.board_view.display()

  @abstractmethod
  def display_win(self):
    """This method displays a statement to the user if they win """
    pass

  @abstractmethod
  def display_loss(self):
    """This method displays a statement to the user if they lost"""
    pass

  @abstractmethod
  def display_play_again(self):
    """This method displays a statement asking the user to play again"""
    pass
  
  @abstractmethod
  def say_goodbye(self):
    """This method displays a statement saying goodbye to the player if they chose to no longer play"""
    pass

  def display_word_to_guess(self,word_to_guess):
    """This method displays the word the player is trying to guess, usually at the end of a game

    Args:
        word_to_guess (str): a string representing the word the player is trying to guess
    """
    pass