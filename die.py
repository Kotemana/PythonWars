from random import randint


class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self, number)->int:
        result = 0
        for i in range(0, number):
            result += randint(1, self.sides)
        return result
