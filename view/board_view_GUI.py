from model.board import board
from view.board_view import BoardView
from view.game_view import GameView
import tkinter as tk
class BoardViewGUI(BoardView):
  """This class is a child class of the BoardView class, and represents the Board Grid in the GUI only 
  """

  #Defines colors of the background and foreground of the the letters based on correctness
  INCORRECT = ('BLACK','WHITE')
  PARTIAL_CORRECT = ('YELLOW','BLACK')
  CORRECT = ('GREEN','BLACK')

  def __init__(self, board: board,root: tk) -> None:
    """This method initializes a instance of the BoardViewGUI class using a inputted argument root (root of tkinter window)
    and a instance of the board classed initalized by the parent class, Board View

    Args:
        board (board): A instance of the board class
        root (tk): A instance of the root of the tkinter window
    """
    super().__init__(board)
    self.root = root

  def display(self):
    """This method displays the board on the root window of the tkinter GUI. It takes in the the amount of lives the player starts with
    from an instance of the player class and the board from an instance of the board class to display the board
    """
    for i in range(self.board.player.lives_start):
        for j in range(self.board.size):
            if self.board.board[i][j][1] == self.board.EMPTY_SLOT:
               Grade = self.INCORRECT
            elif self.board.board[i][j][1] == '!':
               Grade = self.PARTIAL_CORRECT
            elif self.board.board[i][j][1] == '*':
               Grade = self.CORRECT
            label = tk.Label(self.root, text=f"{self.board.board[i][j][0]}",bg=Grade[0],fg=Grade[1], borderwidth=1, relief="solid")
            label.grid(row=i+1, column=j,sticky='nsew',padx=0.5,pady=1)
    for i in range(self.board.player.lives_start):
      self.root.grid_rowconfigure(i, weight=1)  
    self.root.grid_rowconfigure(self.board.player.lives_start, weight=1)
    for j in range(self.board.player.lives_start):
      self.root.grid_columnconfigure(j, weight=1)  

