from view.board_view import BoardView
from view.game_view import GameView
from model.player import player

class GameViewConsole(GameView):
  def __init__(self, board_view: BoardView) -> None:
    super().__init__(board_view)

  def display_lives(self):
    print(f"You have {player.lives_left} attempts left to guess the word")

  def get_guess(self):
    guess = input("Enter your guess:")
    guess = guess.lower()
    return guess

  def display_invalid_guess(self):
    print(f'Guess is not of correct length! Input new guess!')

  def display_winner(self):
    print(f"You guessed the word!")

  def display_draw(self):
    print('Out of attempts. Game over!')