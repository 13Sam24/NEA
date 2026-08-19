import random
import pygame
from Entities.Enemy.Enemy1 import Enemy1

# Block object
class Block:
    def __init__(self, x, y, blockType, screen): # The x and y are the location of the top left corner of the block
        self.location = (x, y)
        self.screen = screen
        self.rect = pygame.Rect(self.location[0], self.location[1], 60, 60)
        if self.location[0] == 3780:
            self.lastBlock = True
        else:
            self.lastBlock = False

        # This will allow for differnet types of blocks to be placed to make the game more visually apealing
        match blockType:
            case 'simple':
                self.type = 'Assets/Blocks/SimpleBlock.png'
            case 'grass':
                self.type = 'Assets/Blocks/GrassBlock.png'
                
        # Placing the block image in the set location
        self.block = pygame.image.load(self.type).convert_alpha()
        self.screen.blit(self.block, self.location)

    def moveBlock(self, num): # This will place a new block in the new loaction. Make sure to re place background as last image will otherwise stay
        self.location = (self.location[0] - num, self.location[1])
        self.screen.blit(self.block, self.location)
        self.rect = pygame.Rect(self.location[0], self.location[1], 60, 60)
        if self.lastBlock and self.location[0] == 1860: # This is needed as if it is the last block in the chunk and it is nearly on the screen a new chunk needs to be made
            ##### IMPORTANT THE == 1860 means that the chunk needs to move an amount that 1860 divides ncely by like 5 and 10
            return True
        else:
            return False
        
    def update(self):
        self.screen.blit(self.block, self.location)


class Chunk:
    def __init__(self, screen, difficutly, seed):
        self.screen = screen
        self.difficutly = difficutly
        self.seed = seed
        self.background = pygame.image.load('Assets/Blocks/Background.png').convert_alpha()
        self.chunklist = []
        self.chunkSizeList = []
        self.enemyList = []
        self.enemySizeList = []

    def seedGenerate(self):
        if self.seed == 'null':
            self.seed = random.randint(0, 1000000) # Sets the seed to a random number if it is equal to null

    def start(self):
        self.screen.blit(self.background, (0, 0))
        chunkSize = 0
        for x in range(0, 1920, 60): # This places in the floor
            self.chunklist.append(Block(x, 1020, 'grass', self.screen))
            chunkSize += 1
        self.chunkSizeList.append(chunkSize) # Ads the amount of blocks to the list

    def makeChunk(self):
        self.screen.blit(self.background, (0, 0))
        nextToBlock = False
        chunkSize = 0
        for y in range(0, 1020, 60): # Y coordinates for the blocks
            for x in range(1920, 3840, 60): # X coordinates for the blocks (it starts of screen)
                if nextToBlock: # Higher chance of placing block if there is already one.
                    num = random.randint(0, 20)
                else:
                    num = random.randint(0, 5)
                
                if num >= 5:
                    self.chunklist.append(Block(x, y, 'grass', self.screen)) # Places a block and adds it to the list
                    nextToBlock = True
                    chunkSize += 1
                else:
                    nextToBlock = False
        for x in range(1920, 3840, 60): # Placing in the floor
            self.chunklist.append(Block(x, 1020, 'grass', self.screen))
            chunkSize += 1
        self.chunkSizeList.append(chunkSize)


        # Places enemeis
        enemyNumber = 0
        for i in range(chunkSize):
            num = random.randint(0, 30)
            if num == 1:
                self.enemyList.append(Enemy1(self.screen, self.chunklist[i].location[0], self.chunklist[i].location[1] - 50))
                enemyNumber += 1
                for j in range(chunkSize):
                    if self.chunklist[i].location[0] == self.chunklist[j].location[0] and self.chunklist[i].location[1] - 50 == self.chunklist[j].location[0]:
                        self.chunklist[j].moveBlock(-1080)
        self.enemySizeList.append(enemyNumber)


    def move(self, distance):
        makingNewChunk = False
        self.screen.blit(self.background, (0, 0))
        for i in range(len(self.chunklist)):
            newChunk = self.chunklist[i].moveBlock(distance) # This moves all the chunks over one

        for i in range(len(self.enemyList)):
            self.enemyList[i].move(distance) # Moves the enemy over

        if newChunk and makingNewChunk == False:
            for j in range(0, self.chunkSizeList[0]):
                del self.chunklist[0]
            del self.chunkSizeList[0]
            for j in range(0, self.enemySizeList[0]):
                del self.enemyList[0]
            del self.enemySizeList[0]
            self.makeChunk()
            makingNewChunk = True
        