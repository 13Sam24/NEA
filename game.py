import random

class Game():
    def __init__(self, difficulty):
        self.difficulty = difficulty
    
    def pickSeed(self, seed):
        if seed == 'null':
            seed = random.randint(0, 100000000)
        random.seed((seed))


game = Game(1)
game.pickSeed('76')
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))