class player: #this class represents the player themselves. 
    """This class represents the player themselves
    """
    def __init__(self,lives=6) -> None:
        """This method initizalizes an instance of the player class. Usually in this program there is only one instance of player

        Args:
            lives (int, optional):The amount of lives the player stats with. Defaults to 6.
        """
        self.lives_start = lives #this serves as a constant of the amount of lives the player has for creation and displaying of the board purposes
        self.lives_left = lives #this keeps track of how many lives the player has left
    
    def life_lost(self)-> None:
        """This method subracts one life from the amount of lives the player has left
        """
        self.lives_left -= 1

    def get_lives_left(self):
        """This function returns the amount of lives the player as left

        Returns:
            lives_left (int): A interger representing how many lives the player has left
        """
        return f'{self.lives_left}'
    
    def reset_lives(self):
        """This method resets the amount of lives the player has left, usually to reset the game after it finishes
        """
        self.lives_left = self.lives_start

    def __str__(self):
        """This method is mostly for debugging, printing the lives left and started with by the player nicely

        Returns:
            str : A string with a nice printed statement of the amount of lives the player started with and has left
        """
        return f'lives started with: {self.lives_start}, lives left {self.lives_left}'

