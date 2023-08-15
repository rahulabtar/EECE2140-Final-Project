#this is the gui view version
import tkinter as tk
from model.game import game
from view.game_view_GUI import GameViewGUI
from view.board_view_GUI import BoardViewGUI
from controller.game_controller import GameController


model = game()
root = tk.Tk()
root.geometry(str(model.board.size*100)+'x'+str(model.board.player.lives_start*50))
root.title("Wordle Board")
board_view = BoardViewGUI(model.board,root)
view = GameViewGUI(board_view,model.board.player,root)

controller = GameController(model, view)
controller.run_game()
root.mainloop()