class player:
    def __init__(self,lives=5) -> None:
        self.lives_start = lives
        self.lives_left = lives
        pass
    def life_lost(self)-> None:
        self.lives -= 1
    def get_lives_left(self):
        return self.lives_left

