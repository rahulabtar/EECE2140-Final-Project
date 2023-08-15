from view.board_view import BoardView
from view.game_view import GameView
from model.player import player
import tkinter as tk

class GameViewGUI(GameView):
  def __init__(self, board_view: BoardView,player:player,root:tk) -> None:
    super().__init__(board_view,player)
    self.root = root

  def display_lives(self):
    Label = tk.Label(self.root, text=f"Lives:{self.player.lives_left}")
    Label.grid(row=self.player.lives_start+1, column=0,columnspan=2)
    pass

  def get_guess(self):
    def guess_clicked():
        guess_value.set(entry.get())  # Set the value of guess_value to the input content
        self.root.quit()  # Exit the mainloop
    guess_value = tk.StringVar()  # Create a StringVar to store the guessed value
    entry = tk.Entry(self.root, textvariable=guess_value)
    entry.grid(row=self.player.lives_start + 1, column=3, columnspan=1, sticky='nwes')
    button = tk.Button(self.root, text="Guess", command=guess_clicked)
    button.grid(row=self.player.lives_start + 1, column=2, columnspan=1, sticky='ne')
    self.root.mainloop()
    return guess_value.get()  # Return the guessed value after the mainloop ends

  def display_invalid_guess(self):
    error = tk.Toplevel(self.root)
    error.title("Error:Invalid Guess")
    
    label = tk.Label(error, text="Invalid word size. Enter word of correct size")
    label.pack(padx=20, pady=20)
    
    close_button = tk.Button(error, text="Close", command=error.destroy)
    close_button.pack(pady=10)
   

  def display_win(self):
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
    def darn_clicked():
      loss_window.destroy()
      self.root.quit()
    loss_window = tk.Toplevel(self.root)
    loss_window.title("You Lost!")
    tk.Label(loss_window, text =f"Out of Attempts, Game Over! The correct word was").pack(padx=20, pady=20)
    close_button = tk.Button(loss_window, text="Darn!", command=darn_clicked)
    close_button.pack(pady=10)
    self.root.mainloop()
    
  
  def display_play_again(self):
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
    again_window = tk.Toplevel(self.root)
    again_window.title("Closing App...")
    tk.Label(again_window, text ="Goodbye!").pack(padx=20, pady=20)
    bye_button = tk.Button(again_window, text="Bye", command=self.root.quit)
    bye_button.pack(pady=10)
    pass