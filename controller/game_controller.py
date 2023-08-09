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
      self.view.display_board()

      guess = self.view.get_guess()
      while not self.model.is_valid_guess(guess):
        self.view.display_invalid_guess()
        guess = self.view.get_guess()

      guess = self.model.get_guess_graded(word_to_guess,guess)
      self.model.board.update_board(guess)
      self.model.player.life_lost()

      if self.model.check_loss():
        self.view.display_loss()
        break
      elif self.model.check_win(guess):
        self.view.display_win()
        break
    self.view.display_board()
    print("The word was", word_to_guess,"!")

      
