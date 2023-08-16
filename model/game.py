from model.board import board
from model.player import player
import random 
class game:
    """This class represents the rules and logic to the game, along with process such as getting and grading words
    """
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
        index = random.randint(1,len(words_to_guess)) #random module used to randomly chose word
        self.word_to_guess = words_to_guess[index]
        return words_to_guess[index]


    def check_win(self,graded_word):
        """This method checks whether the inputed graded word (list with graded chars of guessed word) has all correct
        grades to it. If it does returns True

        Args:
            graded_word (List of lists): The word the player guessed graded

        Returns:
            bool: A boolean that represents whether the player won or not
        """
        for i in range(self.size):
            if graded_word[i][1] != '*':
                return False
        return True 

    
    def check_loss(self):
        """This method checks whether the player as ran out of lives, if so sends false representing a loss

        Returns:
            bool: A boolean representing whether the player loss or not
        """
        if int(self.player.get_lives_left()) == 0:
            return True
        return False

    def is_valid_guess(self,guess):
        """This method checks whether a inputted guess (string) is the correct size to be on the board
        or the same size as the word the player is trying to guess

        Args:
            guess (str): A string representing the players guess

        Returns:
            bool: If true the players guess is valid, if false the players guess is not valid
        """
        if len(guess.strip()) == self.size:
            return True
        return False
    
    def get_guess_graded(self,word,guess): 
        """This method takes a string representing the players guess (guess) and a string the player is trying to guess (word)
        it then compares each index of the two strings and returns a list of charachters and a grade 
        ! represents a partially correct answer (right letter, wrong spot)
        * represetns a correct answer (right letter, right spot)

        Args:
            word (str): A string, the players guess
            guess (str): A string, the word the player is trying to guess

        Returns:
            graded_word (list of lists): A list of lists. The inner list contains a charachter of the string an its corresponding grade
        """
        graded_word = []
        for i in range(self.size):
            graded_word.append(['','']) #creates empty double list of approiate size
        for i in range(self.size): #fills based on correctness
            if guess[i] not in word:
                graded_word[i] = [guess[i],self.board.EMPTY_SLOT]
            elif guess[i] in word and guess[i] != word[i]:
                graded_word[i] = [guess[i],'!']
            elif guess[i] in word and guess[i] == word[i]:
                graded_word[i] = [guess[i],'*'] 
        return graded_word
    
    def play_again(self,ans):
        """This function tells whether the player wants to player again

        Args:
            ans (bool): whether the player wants to play again or not

        Returns:
            bool: whether the player wants to play again or not
        """
        if ans == True:
            return True
        else:
            return False


        
