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

    def move(self, num):
        self.location = (self.x - num, self.y)
        self.block = pygame.image.load(self.type).convert_alpha()
        self.screen.blit(self.block, self.location)


class Chunk:
    def __init__(self, screen, difficutly, seed):
        self.screen = screen
        self.difficutly = difficutly
        self.seed = seed
        self.chunk = []

    def seedGenerate(self):
        if self.seed == 'null':
            self.seed = int(random.randint(0, 1000000))
        return self.seed

    def start(self):
        background = pygame.image.load('Assets/Blocks/Background.png').convert_alpha()
        self.screen.blit(background, (0, 0))
        for x in range(0, 1920, 60):
            self.chunk.append(Block(x, 1020, 'simple', self.screen))

    def makeChunk(self):
        background = pygame.image.load('Assets/Blocks/Background.png').convert_alpha()
        self.screen.blit(background, (0, 0))
        nextToBlock = False
        for y in range(0, 1020, 60):
            for x in range(0, 1920, 60):
                if nextToBlock:
                    num = random.randint(0, 1)
                else:
                    num = random.randint(0, 5)
                
                if num == 1:
                    self.chunk.append(Block(x, y, 'simple', self.screen))
                    nextToBlock = True
                else:
                    nextToBlock = False
        for x in range(0, 1920, 60):
            self.chunk.append(Block(x, 1020, 'simple', self.screen))
        self.run = False
    def move(self, num):
        
        for i in range(len(self.chunk)):
            self.chunk[i].move(1)