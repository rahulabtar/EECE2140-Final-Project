from view.board_view import BoardView
from view.game_view import GameView
from model.player import player

class GameViewConsole(GameView):
  def __init__(self, board_view: BoardView,player:player) -> None:
    super().__init__(board_view,player)

  def display_lives(self):
    print(f"You have {self.player.get_lives_left()} attempts left to guess the word")

  def get_guess(self):
    guess = input("Enter your guess:")
    guess = guess.lower()
    return guess

  def display_invalid_guess(self):
    print(f'Guess is not of correct length! Input new guess!')

  def display_win(self):
    print(f"You guessed the word!")

  def display_loss(self):
    print('Out of attempts. Game over!')
  
  def display_play_again(self):
    ans = input('Play again? Type Y to play again, type anything else to exit game')
    if ans =='Y': ans = True
    else: ans = False
    return ans
  
  def say_goodbye(self):
    print('Goodbye!')