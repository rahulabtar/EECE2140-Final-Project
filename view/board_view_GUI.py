from model.board import board
from view.board_view import BoardView
from view.game_view import GameView
import tkinter as tk
class BoardViewGUI(BoardView):
  INCORRECT = ('BLACK','WHITE')
  PARTIAL_CORRECT = ('YELLOW','BLACK')
  CORRECT = ('GREEN','BLACK')

  def __init__(self, board: board) -> None:
    super().__init__(board)
    self.root = tk.Tk()
    self.GameView = GameView()

  def display(self):
    #root = tk.Tk()
    tk.Button(text='Input Guess:',command=self.GameView.get_guess).grid(row=0,column=0)
    WordInput = tk.Entry(self.root)
    WordInput.grid(row=0,column=1)
    for i in range(self.board.player.lives_start):
        for j in range(self.board.size):
            if self.board.board[i][j][1] == self.board.EMPTY_SLOT:
               Grade = self.INCORRECT
            elif self.board.board[i][j][1] == '!':
               Grade = self.PARTIAL_CORRECT
            elif self.board.board[i][j][1] == '*':
               Grade = self.CORRECT
            label = tk.Label(self.root, text=f"{self.board.board[i][j][0]}",bg=Grade[0],fg=Grade[1], borderwidth=1, relief="solid")
            label.grid(row=i+1, column=j)
    self.root.title("Wordle")
    self.root.mainloop()
