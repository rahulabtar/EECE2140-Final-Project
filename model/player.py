class player:
    def __init__(self,lives=6) -> None:
        self.lives_start = lives
        self.lives_left = lives
        pass
    def life_lost(self)-> None:
        self.lives_left -= 1
    def get_lives_left(self):
        return f'{self.lives_left}'
    def reset_lives(self):
        self.lives_left = self.lives_start
    def __str__(self):
        return f'lives started with: {self.lives_start}, lives left {self.lives_left}'

