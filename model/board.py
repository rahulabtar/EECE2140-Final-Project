from model.player import player

class board: #This class represents the board or grid that holds the words
    """This class represents the board, and has to do with storing and manipulating guess data
    """

    EMPTY_SLOT = ' ' #Defines what an empty slot is considered as a class attribute

    def __init__(self,player: player,size:int=5) -> None:
        """This method initizalizes an instance of the board class with an instance of the player class and a given size 
        as attributes. Changing size changes the size of the board everywhere in the program

        Args:
            player (player): A instance of the player class
            size (int): A given interger representing the size of the board; the length of the word the player is guessing
        """
        self.size = size
        self.player = player
        self.board = [[[self.EMPTY_SLOT, self.EMPTY_SLOT] for j in range(self.size)] for i in range(self.player.lives_start)]
        #the above attribute self.board is an an attribute storing all the data of the board, such as the words guessed by row
        #the chars in each word guessed, and the grade of the chars in a list of list of lists
        #innermost list, a char, and its grade
        #middle list, a list of the innermost lists, a char and its grade. Each index represents a word
        # a list of all the words. Each index represnets a grid of the board
        #self.board creates the board with all empty slots to be later filled. 

    def update_board(self,guess_graded:list):
        """This method updates the attribute board. With the last guess made by the player graded

        Args:
            guess_graded (list): The guess graded. A list of lists, inner list char w/ grade. Outter list is each char of word w/grade
        """
        index = self.player.lives_start - int(self.player.get_lives_left()) #calcs index of which list affecting
        #The above line of code calcs the index of which row of the board to change. Does this based on the lives the player has left
        #ex: 5 lives left causes row 0 to be indexed. 5 lives causes row 0 to be indexed.
        self.board[index] = guess_graded #sets row indexed to graded guess
    
    
    def clear_board(self):
        self.board = [[[self.EMPTY_SLOT, self.EMPTY_SLOT] for j in range(self.size)] for i in range(self.player.lives_start)]
        """This method clears the board attribute, usually called to reset the game 
        """

    def __str__(self):
        """This method allows the attributes of the board to be printed nicely, usually for debugging
        Returns:
            str: A string nicely displaying the attributes of the instance of the board
        """
        return f"Size of Words/Board: {self.size}, Board: {self.board}"