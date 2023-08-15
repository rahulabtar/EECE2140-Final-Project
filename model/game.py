from model.board import board
from model.player import player
import random 
class game:
    def __init__(self,size=5) -> None:
        """Initizizes the game class, with size being the size of the board established in the board class
        """
        self.size = size
        self.player = player()
        self.board = board(self.player,size)
        self.word_to_guess = None       
        pass

    def get_all_words_of_size(self)->list:
        """This method takes in a requested size of the word (from the board class) and makes a list of all the words in the 1000 most common words in the english language text file that have the size

        Args:
            size (int): the size of the board, of the word

        Returns:
            words_to_guess (list): A list of all the words in the text file of length size. Ex: Size = 5, words will be 5 letters long
        """
        words_to_guess = []
        with open('1-1000.txt','r') as file:
            for line in file:
                word = line.strip('\n')
                if len(word) == self.size:
                    words_to_guess.append(word)
        return words_to_guess
    
    def pick_word_to_guess(self,words_to_guess:list):
        """This method picks a random word for the player to guess based on a inputted list of words

        Args:
            words_to_guess (list): A list of words from the get_all_words_of_size method

        Returns:
            word (str): The word the user has to guess of size 
        """
        index = random.randint(1,len(words_to_guess))
        self.word_to_guess = words_to_guess[index]
        return words_to_guess[index]


    def check_win(self,graded_word):
        for i in range(self.size):
            if graded_word[i][1] != '*':
                return False
        return True 

    
    def check_loss(self):
        if int(self.player.get_lives_left()) == 0:
            return True
        return False

    def is_valid_guess(self,guess):
        if len(guess.strip()) == self.size:
            return True
        return False
    
    def get_guess_graded(self,word,guess): #a cleaner way to get the results needed, in one simple function. Uses branch system
        graded_word = []
        for i in range(self.size):
            graded_word.append(['',''])
        for i in range(self.size):
            if guess[i] not in word:
                graded_word[i] = [guess[i],self.board.EMPTY_SLOT]
            elif guess[i] in word and guess[i] != word[i]:
                graded_word[i] = [guess[i],'!']
            elif guess[i] in word and guess[i] == word[i]:
                graded_word[i] = [guess[i],'*'] 
        return graded_word
    
    def play_again(self,ans):
        if ans == True:
            return True
        else:
            return False


        
