from model.game import game
from view.game_view import GameView

class GameController: #This connects the model and chosen view to control them
  """This class represents the connection between the model and chosen view. 
  it is in charge of running the game, and connecting the rules and logic of the game to the classes that display
  information to the user
  """


  def __init__(self, model: game, view: GameView) -> None:
    """This method initializes the game class when called with a given instance of the game and game view class as attributes

    Args:
        model (game): A instance of the game class, contains instances of board and player class as attributes
        view (GameView): A instance of the gameview class, contains instances of boardview class as attribute
    """
    self.model = model
    self.view = view

  def run_game(self):
    """This method is in charge of running the game by calling methods defined by the model and view. 
    """

    #GAME LOOP BEGINS HERE

    while True: #This while loop allows the game to loop until the player chooses to not play anymore
      
      #The first thing the game does is display the board, lives, and chooses a word the player needs to guess
      self.view.display_board()
      self.view.display_lives()
      word_to_guess = self.model.pick_word_to_guess(self.model.get_all_words_of_size()) 
      #above lines stores word to guess that was chosen randomly by the game

      
      #GUESSING PROCESS LOOP BEGINS HERE

      while True: #This while loop begins the guessing process for the player. It continues until the player runs out of lives or guesses the word
        
        #This code gets a valid guess from the user based on the current view method chosen
        guess = self.view.get_guess()
        while not self.model.is_valid_guess(guess): #does not let program progress until valid guess is given
          self.view.display_invalid_guess()
          guess = self.view.get_guess() #stores guess as guess var

        #This code grades the guess, displays the guess and its grade on the board and takes away one life from the player
        guess = self.model.get_guess_graded(word_to_guess,guess)
        self.model.board.update_board(guess)
        self.model.player.life_lost()

        #displays the above changes via the view to the player
        self.view.display_board()
        self.view.display_lives()

        #checks to see if the last guess made by the player was the correct guess, or if player is out of lives
        if self.model.check_win(guess):
          self.view.display_win() #displays win
          #if it is breaks out of the guessing process loop
          break
        elif self.model.check_loss(): #if player is out of lives displays loss and breaks out of guessing process loop
          self.view.display_loss()
          break

      #GUESSING PROCESS LOOP ENDS HERE

      #displays the board one last time for the player to see proof of there win or loss
      self.view.display_board()
      #displays the correct word to the player
      self.view.display_word_to_guess(word_to_guess)
      
      #asks the player if they would like to play again, and resets the board and the player lives
      ans = self.view.display_play_again()
      self.model.board.clear_board()
      self.model.player.reset_lives()

      #if the answer is no a goodbye message is show and the game loop is broken out of 
      if not self.model.play_again(ans):
        self.view.say_goodbye() 
        break #game loop broken out of, quittting game

    # GAME LOOP ENDS HERE
        

      

      
