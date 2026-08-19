import pygame

pygame.font.init()
fontName = pygame.font.get_default_font()
font = pygame.font.Font(fontName, 30)

class Player:
    def __init__(self, screen, locationX, locationY):
        self.screen = screen
        self.idleImage = pygame.image.load('Assets/Entities/player.png').convert_alpha()
        self.location = (locationX, locationY)
        self.screen.blit(self.idleImage, self.location)
        self.jumping = False
        self.jumpingVelocity = 0
        self.rect = pygame.Rect(self.location[0], self.location[1],55, 55)
        self.health = 100


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
        self.rect = pygame.Rect(self.location[0], self.location[1], 59, 59)

    def jump(self):
        self.location = (self.location[0], self.location[1] - self.jumpingVelocity)
        self.screen.blit(self.idleImage, self.location)

    def fall(self):
        self.location = (self.location[0], self.location[1] + 5)
        self.screen.blit(self.idleImage, self.location)

    def checkCollision(self, blockList, distanceX, distanceY):
        collide = False
        self.rect = pygame.Rect(self.location[0] + distanceX, self.location[1] - distanceY, 59, 59)
        for i in range(len(blockList)):
            if self.rect.colliderect(blockList[i].rect):
                collide = True
        return collide

    def hold(self):
        print('hold ont object')

    def displayHealth(self):
        if self.health >= 50:
            healthText = font.render(str(self.health), False, (0, 0, 0))
            self.screen.blit(healthText, (10, 5))
        elif self.health >= 15:
            healthText = font.render(str(self.health), False, (255, 165, 0))
            self.screen.blit(healthText, (10, 5))
        else:
            healthText = font.render(str(self.health), False, (255, 0, 0))
            self.screen.blit(healthText, (10, 5))