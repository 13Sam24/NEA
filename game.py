import random
import pygame

# Block object
class Block:
    def __init__(self, x, y, blockType, screen): # The x and y are the location of the top left corner of the block
        self.location = (x, y)
        self.screen = screen
        if self.location[0] == 3780:
            self.lastBlock = True
        else:
            self.lastBlock = False
    

        # This will allow for differnet types of blocks to be placed to make the game more visually apealing
        match blockType:
            case 'simple':
                self.type = 'Assets/Blocks/SimpleBlock.png'
                
        # Placing the block image in the set location
        self.block = pygame.image.load(self.type).convert_alpha()
        self.screen.blit(self.block, self.location)

    def moveBlock(self, num):
        self.location = (self.location[0] - num, self.location[1])
        self.block = pygame.image.load(self.type).convert_alpha()
        self.screen.blit(self.block, self.location)
        if self.lastBlock and self.location[0] == 1860:
            return True
        else:
            return False



class Chunk:
    def __init__(self, screen, difficutly, seed):
        self.screen = screen
        self.difficutly = difficutly
        self.seed = seed
        self.chunklist = []
        self.chunkSizeList = []
    def seedGenerate(self):
        if self.seed == 'null':
            self.seed = int(random.randint(0, 1000000))
        return self.seed

    def start(self):
        background = pygame.image.load('Assets/Blocks/Background.png').convert_alpha()
        self.screen.blit(background, (0, 0))
        chunkSize = 0
        for x in range(0, 1920, 60):
            self.chunklist.append(Block(x, 1020, 'simple', self.screen))
            chunkSize += 1
        self.chunkSizeList.append(chunkSize)


    def makeChunk(self):
        background = pygame.image.load('Assets/Blocks/Background.png').convert_alpha()
        self.screen.blit(background, (0, 0))
        nextToBlock = False
        chunkSize = 0
        for y in range(0, 1020, 60):
            for x in range(1920, 3840, 60):
                if nextToBlock:
                    num = random.randint(0, 1)
                else:
                    num = random.randint(0, 5)
                
                if num == 1:
                    self.chunklist.append(Block(x, y, 'simple', self.screen))
                    nextToBlock = True
                    chunkSize += 1
                else:
                    nextToBlock = False
        for x in range(1920, 3840, 60):
            self.chunklist.append(Block(x, 1020, 'simple', self.screen))
            chunkSize += 1
        self.chunkSizeList.append(chunkSize)

    def move(self, num):
        makingNewChunk = False
        background = pygame.image.load('Assets/Blocks/Background.png').convert_alpha()
        self.screen.blit(background, (0, 0))
        for i in range(len(self.chunklist)):
            newChunk = self.chunklist[i].moveBlock(num)
            if newChunk and makingNewChunk == False:
                for j in range(self.chunkSizeList[0]):
                    del self.chunklist[j]
                print(len(self.chunklist))
                self.makeChunk()
                makingNewChunk = True