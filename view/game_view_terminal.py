from view.board_view import BoardView
from view.game_view import GameView
from model.player import player

class GameViewConsole(GameView):
  """This class represents the game view for the console user interface.
  It is a child class of the GameView class
  """

  def __init__(self, board_view: BoardView,player:player) -> None:
    """This method initializes an instance of this class using the constructor from the parent class

    Args:
        board_view (BoardView): An instance of the BoardView class
        player (player): A instance of the player class
    """
    super().__init__(board_view,player)

  def display_lives(self):
    """This method displays the amount of lives the player has left using print function by refering to the instance of the player class
    """
    print(f"You have {self.player.get_lives_left()} attempts left to guess the word")

  def get_guess(self):
    """This method gets a guess from the player using the input function, and converts into all lower case

    Returns:
        guess (str): the players guess
    """
    guess = input("Enter your guess:")
    guess = guess.lower()
    return guess

  def display_invalid_guess(self):
    """This method displays a error message if the players guess is invalid using the print function
    """
    print(f'Guess is not of correct length! Input new guess!')

  def display_win(self):
    """This method displays a win message if the player guesses the right word using the print function
    """
    print(f"You guessed the word!")

  def display_loss(self):
    """This method displays a loss message if the player runs out of lives using the print function
    """
    print('Out of attempts. Game over!')
  
  def display_play_again(self):
    """This method asks the player if they want to play again using input(), returns true or false"""
    ans = input('Play again? Type Y to play again, type anything else to exit game')
    if ans =='Y': ans = True
    else: ans = False
    return ans
  
  def say_goodbye(self):
    """This method prints out a goodbye message at the end of a game using the print function
    """
    print('Goodbye!')

  def display_word_to_guess(self,word_to_guess):
    """This method prints out the word the player is tring to guess using the print function and the given word the player is trying to guess

    Args:
        word_to_guess (str): The word the player is trying to guess
    """
    print('The word was ', word_to_guess)