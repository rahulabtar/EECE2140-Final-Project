from model.game import game
from view.game_view import GameView

class GameController:
  def __init__(self, model: game, view: GameView) -> None:
    self.model = model
    self.view = view

  def run_game(self):
    word_to_guess = self.model.pick_word_to_guess(self.model.get_all_words_of_size())
    while True:
      self.view.display_lives()

      guess = self.view.get_guess()
      while not self.model.is_valid_guess(guess):
        self.view.display_invalid_guess()
        guess = self.view.get_guess()

      guess = self.model.get_guess_graded(word_to_guess,guess)
      self.model.board.update_board(guess)

      if self.model.check_win():
        self.view.display_win()
        break
      elif self.model.check_loss():
        self.view.display_loss()
        break

      self.model.player.life_lost()
