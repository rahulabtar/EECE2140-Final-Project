from model.game import game
from view.game_view import GameView

class GameController:
  def __init__(self, model: game, view: GameView) -> None:
    self.model = model
    self.view = view

  def run_game(self):
    while True:
      self.view.display_board()
      self.view.display_lives()
      word_to_guess = self.model.pick_word_to_guess(self.model.get_all_words_of_size())
      while True:
        
        guess = self.view.get_guess()
        while not self.model.is_valid_guess(guess):
          self.view.display_invalid_guess()
          guess = self.view.get_guess()

        guess = self.model.get_guess_graded(word_to_guess,guess)
        self.model.board.update_board(guess)
        self.model.player.life_lost()

        self.view.display_board()
        self.view.display_lives()

        if self.model.check_win(guess):
          self.view.display_win()
          break
        elif self.model.check_loss():
          self.view.display_loss()
          break
        

      self.view.display_board()
      self.view.display_word_to_guess(word_to_guess)
      
      ans = self.view.display_play_again()
      self.model.board.clear_board()
      self.model.player.reset_lives()
     
      if not self.model.play_again(ans):
        self.view.say_goodbye()
        break
    
        

      

      
