import random
import pygame
import time

class Block:
    def __init__(self, x, y, blockType, screen):
        self.location = (x, y)
        self.screen = screen

        match blockType:
            case 'simple':
                self.type = 'Assets/Blocks/SimpleBlock.png'

        self.block = pygame.image.load(self.type).convert_alpha()
        self.screen.blit(self.block, self.location)


def game(screen, difficulty, seed):
    chunk = []
    background = pygame.image.load('Assets/Blocks/Background.png').convert_alpha()
    screen.blit(background, (0, 0))
    
    
    if seed == 'null':
        seed = random.randint(0, 100000000)
    random.seed((seed))


    # this code does not work
    # x = 72
    # x = 32
    # y = 64
    # y = 18
    # for i in range(x):
        # for j in range(y):
            # num = random.randint(0, 1)
            # if num == 1:
                # chunk.append(Block(i * y, j * x, difficulty, screen))






    ## Attempt 2 THis works
    # each block is 60 x 60
    # nextToBlock = False
    # for x in range(0, 1920, 60): #This is the x axis
    #     for y in range(0, 1020, 60): #this is the y axix
    #         if nextToBlock:
    #             num = random.randint(0, 1)
    #         else:
    #             num = random.randint(0, 5)
            
    #         if num == 1:
    #             chunk.append(Block(x, y, 'simple', screen))
    #             nextToBlock = True
    #         else:
    #             nextToBlock = False

    # for x in range(0, 1920, 60):
    #     chunk.append(Block(x, 1020, 'simple', screen))



    # Attempt 3
    nextToBlock = False
    for y in range(0, 1020, 60):
        for x in range(0, 1920, 60):
            if nextToBlock:
                num = random.randint(0, 1)
            else:
                num = random.randint(0, 5)
            
            if num == 1:
                chunk.append(Block(x, y, 'simple', screen))
                nextToBlock = True
            else:
                nextToBlock = False
        chunk.append(Block(x, 1020, 'simple', screen))
    return

        # on hardest difficulty it could be that sometiems the floor is missing