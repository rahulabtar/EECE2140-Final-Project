import unittest
from model.game import game

class Test_(unittest.TestCase):
    def test_check_win(self):
        self.assertEqual(game.check_win([[0,'*'],[0,'*'],[0,'*'],[0,'*'],[0,'*']]),True)
        self.assertEqual(game.check_win([[0,'*'],[0,'*'],[0,'*'],[0,'*'],[0,'!']]),False)
        self.assertEqual(game.check_win([[0,'*'],[0,'*'],[0,'*'],[0,'3'],[0,'*']]),False)
    def test_get_guess_graded(self):
        self.assertEqual(game.get_guess_graded('tests','tests'),[['t','*'],['e','*'],['s','*'],['t','*'],['s','*']])
        self.assertEqual(game.get_guess_graded('testa','tests'),[['t','*'],['e','*'],['s','*'],['t','*'],['s','!']])
        self.assertEqual(game.get_guess_graded('tests','testa'),[['t','*'],['e','*'],['s','*'],['t','*'],['a','']])
        self.assertEqual(game.get_guess_graded('Tests','tests'),[['t',''],['e','*'],['s','*'],['t',''],['s','*']])
    def test_is_valid_guess(self):
        self.assertEqual(game.is_valid_guess('words'),True)
        self.assertEqual(game.is_valid_guess('word'),False)
        self.assertEqual(game.is_valid_guess('wordsd'),False)
        
        
