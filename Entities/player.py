import pygame
class Player:
    def __init__(self, screen, locationX, locationY):
        self.screen = screen
        self.idleImage = pygame.image.load('Assets/Entities/player.png').convert_alpha()
        self.location = (locationX, locationY)
        self.screen.blit(self.idleImage, self.location)
        self.jumping = False



    def move(self, speed):
        if speed > 0:
            #move forwards
            self.location = (self.location[0] + speed, self.location[1])
        else:
            #move Backwards
            #if self.location[0] > 0:
            self.location = (self.location[0] - speed, self.location[1])
            
        self.screen.blit(self.idleImage, self.location)

    def jump(self):
        if self.jumping == False:
            for i in range(0, 120):
                self.location = (self.location[0], self.location[1] - 1)
                self.screen.blit(self.idleImage, self.location)
                self.jumping = True
        

    def hold(self):
        print('hold ont object')