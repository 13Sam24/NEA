import random
import pygame

# Block object
class Block:
    def __init__(self, x, y, blockType, screen): # The x and y are the location of the top left corner of the block
        self.location = (x, y)
        self.screen = screen

        # This will allow for differnet types of blocks to be placed to make the game more visually apealing
        match blockType:
            case 'simple':
                self.type = 'Assets/Blocks/SimpleBlock.png'
                
        # Placing the block image in the set location
        self.block = pygame.image.load(self.type).convert_alpha()
        self.screen.blit(self.block, self.location)


def game(screen, difficulty, seed):
    chunk = []
    background = pygame.image.load('Assets/Blocks/Background.png').convert_alpha()
    screen.blit(background, (0, 0))
    
    
    if seed == 'null':
        seed = random.randint(0, 100000000)
    random.seed((int(seed)))

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
    for x in range(0, 1920, 60):
        chunk.append(Block(x, 1020, 'simple', screen))

    return

        # on hardest difficulty it could be that sometiems the floor is missing