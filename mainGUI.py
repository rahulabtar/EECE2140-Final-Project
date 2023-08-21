#this main file is in charge of connecting the various classes of the game together to help run the code
import tkinter as tk
from model.game import game
from view.game_view_GUI import GameViewGUI #sets view to be GUI child classes of view
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