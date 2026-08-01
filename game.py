import random
import pygame


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

    
    for i in range(36):
        for j in range(32):
            num = random.randint(0, 1)
            if num == 1:
                chunk.append(Block(j * 32, i * 36, difficulty, screen))


        #the world is split into blocks about 30 wide.
        # this means that there are 64 along the bottom and 36 tall
        # each chunk will be 32 in size and 36 tall meaning 2 chunks per screen.
        #

        # on hardest difficulty it could be that sometiems the floor is missing


        #self.screen.blit(self.background, (0, 0))