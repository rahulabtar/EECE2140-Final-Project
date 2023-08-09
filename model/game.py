from model.board import board
from model.player import player
import random 
class game:
    def __init__(self,size=5) -> None:
        """Initizizes the game class, with size being the size of the board established in the board class
        """
        self.size = size
        self.board = board(size)
        self.player = player()
        
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
        return words_to_guess[index]
    
    def get_word_dict(self,word:str)->dict:
        """This method gets a word as a string and returns a dictionary of the charachters of the word as the key and the indexes of the occurence of these charachters as a list as the value

        Args:
            word (str): A word string, usually the word the players is trying to guess or the players guess itself.

        Returns:
            word_dict (dict): The inputted word as a dictionary, with the key being a charachter of the word and the value being a list of all the indexes of the occurences of that charachter in the string
        """
        word_dict = {}
        for char2 in word:
            letter = char2
            positions = []
            for index, char in enumerate(word):
                if char == letter:
                    positions.append(index)
            word_dict[char2] = set(positions)
        return word_dict
       

    def compare_dicts(self,word:str,guess:str)->list:
        """This method takes in two dicts that represent a word and a guess finds the letters the two dicts have in common

        Args:
            word (str): A word as a dictionary, usually with the 
            guess (str): The users guess as a dicitonary, as a dicitonary from the get_word_dict method

        Returns:
            letters_in_common (list): A list of all the letters in common between the word and the guess
        """
        letters_in_common = []
        for key in guess:
            if key in word:
                letters_in_common.append(key)
        return letters_in_common

    def check_indexes(self,word,guess,letters_in_common)->list:
        """This method takes the word and guess as a dictionary and the letters they have in common as a list and returns a list with all the indexes of the guessed word that are in the correct spot as a list of intergers

        Args:
            word (dict): The word the player is trying to guess a dictionary outputted by the get_word_dict function
            guess (dict): The word the player is guessing as a dictionary outputted for the get_word_dict function
            letters_in_common (list): A list of the letters of the word the player is trying to guess and the word the player is guessing that both words have in common as a list 

        Returns:
            correct_indexes (list): A list of the indexes of the players guess that are both the correct letter and are in the correct word.
        """
        right_indexes, letters_correct = [], []
        for element in letters_in_common:
            if word[element] & guess[element] != set():
                right_indexes.append(word[element] & guess[element])
                letters_correct.append(element)
        return [int(element) for subset in right_indexes for element in subset]
    
    def check_win(self,correct_indexes):
        if len(correct_indexes) == self.size:
            return True
        return False
    
    def check_loss(self):
        if self.player.get_lives_left() <= 0:
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

        
