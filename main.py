from model.game import game
from view.game_view_terminal import GameViewConsole
from view.board_view_terminal import BoardViewConsole
from controller.game_controller import GameController

model = game()
player = model.board.player
board_view = BoardViewConsole(model.board)
view = GameViewConsole(board_view,player)

controller = GameController(model, view)
controller.run_game()
