from model.board import board
from model.game import game
from model.player import player

from view.board_view_terminal import BoardViewConsole

board = board()
#print(board)

game = game(board.size)
#print(game)

#main_player = player(4)
#print(main_player)
corr_word = game.pick_word_to_guess(game.get_all_words_of_size())


guess = 'swage'

guess1_graded = game.get_guess_graded(corr_word,guess)
board.update_board(guess1_graded)


guess = 'buddy'

guess1_graded = game.get_guess_graded(corr_word,guess)

#remove life between rounds
board.player.life_lost()


#main_player.life_lost()
#print(main_player)
board_view = BoardViewConsole(board)


board.update_board(guess1_graded)
board_view.display()

