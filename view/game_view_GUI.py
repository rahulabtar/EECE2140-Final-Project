from view.board_view import BoardView
from view.game_view import GameView
from model.player import player
import tkinter as tk

class GameViewGUI(GameView):
  def __init__(self, board_view: BoardView,player:player) -> None:
    super().__init__(board_view,player)

  def display_lives(self):
    pass

  def get_guess(self):
    pass

  def display_invalid_guess(self):
    pass

  def display_win(self):
    pass

  def display_loss(self):
    pass
  
  def display_play_again(self):
    pass
    #return ans
  def say_goodbye(self):
    pass