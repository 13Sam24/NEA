import pygame
class Player:
    def __init__(self, screen, locationX, locationY):
        self.screen = screen
        self.idleImage = pygame.image.load('Assets/Entities/player.png').convert_alpha()
        self.location = (locationX, locationY)
        self.screen.blit(self.idleImage, self.location)
        self.jumping = False
        self.jumpingVelocity = 0
        self.rect = pygame.Rect(self.location[0], self.location[1], 60, 60)


    def move(self, speed):
        if speed > 0:
            #move forwards
            self.location = (self.location[0] + speed, self.location[1])
        else:
            #move Backwards
            if self.location[0] > 0:
                self.location = (self.location[0] + speed, self.location[1])

        self.screen.blit(self.idleImage, self.location)
        #self.rect = pygame.Rect((self.location[0], self.location[0] + 60), (self.location[1], self.location[1] + 60))
        self.rect = pygame.Rect(self.location[0], self.location[1], 60, 60)

    def jump(self):
        self.location = (self.location[0], self.location[1] - self.jumpingVelocity)
        self.screen.blit(self.idleImage, self.location)

    def checkCollision(self, blockList):
        collide = False
        for i in range(len(blockList)):
            if self.rect.colliderect(blockList[i].rect):
                print(f'Player {self.rect}')
                print(f'Block {blockList[i].rect}')
                collide = True
        return collide

    def hold(self):
        print('hold ont object')