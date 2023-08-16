from view.board_view import BoardView
from view.game_view import GameView
from model.player import player
import tkinter as tk

class GameViewGUI(GameView):
  """This class is a GUI child class of the GameView class. It is in charge of displaying all the interactions between the game and the user that aren't the board
  . It manipulates the same root window as the Board_view_GUi class when fed the same root window as an argument
  """

  def __init__(self, board_view: BoardView,player:player,root:tk) -> None:
    """This method initializes and instance of the GameViewGUI class

    Args:
        board_view (BoardView): A instance of the parent class BoardView used to instantiate the attributes of the class
        player (player): A instance of the player class
        root (tk): A instance of the tk class, representing the root window the GameViewGUI class will manipulate. Same window the Board View GUI class manipulates
    """
    super().__init__(board_view,player)
    self.root = root

  def display_lives(self):
    """This method displays a label on the root window that shows the amount of lives the player has left.
    """
    Label = tk.Label(self.root, text=f"Lives:{self.player.lives_left}")
    Label.grid(row=self.player.lives_start+1, column=0,columnspan=2)
    pass

  def get_guess(self):
    """This method creates a entry region and button the user can use to input guesses. Clicking the button returns the text in the entry field, and closes the window to refresh it
    """
    def guess_clicked():
        guess_value.set(entry.get())  # Set the value of guess_value to the input content
        self.root.quit()  # Exit the mainloop
    guess_value = tk.StringVar()  # Create a StringVar to store the guessed value
    entry = tk.Entry(self.root, textvariable=guess_value,width=5)
    entry.grid(row=self.player.lives_start + 1, column=3, columnspan=1, sticky='nwes')
    button = tk.Button(self.root, text="Guess", command=guess_clicked)
    button.grid(row=self.player.lives_start + 1, column=2, columnspan=1, sticky='nwes')
    self.root.mainloop()
    return guess_value.get()  # Return the guessed value after the mainloop ends

  def display_invalid_guess(self):
    """This method creates a pop up window with a close button and error message label for when the player inputs in an invalid guess
    """
    error = tk.Toplevel(self.root)
    error.title("Error:Invalid Guess")
    
    label = tk.Label(error, text="Invalid word size. Enter word of correct size")
    label.pack(padx=20, pady=20)
    
    close_button = tk.Button(error, text="Close", command=error.destroy)
    close_button.pack(pady=10)
   

  def display_win(self):
    """This method creates a pop up window with a close button and a win message label for when the player guesses the correct word
    """
    def woohoo_clicked():
      won_window.destroy()
      self.root.quit()
    won_window = tk.Toplevel(self.root)
    won_window.title("You won!")
    tk.Label(won_window, text ="Congrats, You guessed the word!").pack(padx=20, pady=20)
    close_button = tk.Button(won_window, text="Woohoo!", command=woohoo_clicked)
    close_button.pack(pady=10)
    self.root.mainloop()
  

  def display_loss(self):
    """This method creates a pop up window with a close button and a loss message label for when the player runs out of lives
    """
    def darn_clicked():
      loss_window.destroy()
      self.root.quit()
    loss_window = tk.Toplevel(self.root)
    loss_window.title("You Lost!")
    tk.Label(loss_window, text =f"Out of Attempts, Game Over!").pack(padx=20, pady=20)
    close_button = tk.Button(loss_window, text="Darn!", command=darn_clicked)
    close_button.pack(pady=10)
    self.root.mainloop()
    
  
  def display_play_again(self):
    """This method creates a pop up window that asks the player if they would like to play again. If the yes button is clicked True is returned if the no button is clicked False is returned
    """
    def act_to_yes():
      ans.set(True)  # Set the value of guess_value to the input content
      again_window.destroy()
      self.root.quit()
    
    def act_to_no():
      ans.set(False)
      again_window.destroy()
      self.root.quit()

    ans = tk.BooleanVar(value=False) 
    again_window = tk.Toplevel(self.root)
    again_window.title("Continue?")

    tk.Label(again_window, text ="Would you like to play again?").pack(padx=20, pady=20)
    yes_button = tk.Button(again_window, text="Yes", command=act_to_yes)
    yes_button.pack(pady=10)
    no_button = tk.Button(again_window, text="No", command=act_to_no)
    no_button.pack(pady=20)

  
    again_window.mainloop()
    return ans.get()
  
  def say_goodbye(self):
    """This method creates a pop up window that says goodbye to the user if they choose to no long player the game
    """
    again_window = tk.Toplevel(self.root)
    again_window.title("Closing App...")
    tk.Label(again_window, text ="Goodbye!").pack(padx=20, pady=20)
    bye_button = tk.Button(again_window, text="Bye", command=self.root.quit)
    bye_button.pack(pady=10)
    pass

  def display_word_to_guess(self,word_to_guess):
    """This method displays the word the player is trying to guess nicely in a pop window

    Args:
        word_to_guess (str): The word is trying to play
    """
    def ok_clicked():
      word_to_guess_window.destroy()
      word_to_guess_window.quit()
    word_to_guess_window= tk.Toplevel(self.root)
    word_to_guess_window.title("The answer was...")
    tk.Label(word_to_guess_window, text ="The word was " + word_to_guess + "!").pack(padx=20, pady=20)
    bye_button = tk.Button(word_to_guess_window, text="ok", command=ok_clicked)
    bye_button.pack(pady=10)
    self.root.mainloop()