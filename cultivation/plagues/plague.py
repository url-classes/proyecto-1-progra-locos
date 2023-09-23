import random


class Plague:
    def __init__(self):
        self.activity_Lvl = 100
        self.target_row = random.randint(0, 9)
        self.target_col = random.randint(0, 9)
        self.damage_streak = 0

    def plague_attack(self, ground_matrix: []):
        ground_matrix[self.target_row][self.target_col].health_lvl -= self.damage_streak
