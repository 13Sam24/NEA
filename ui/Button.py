import pygame

class Button:
    def __init__(self, screen, x, y, w, h, image):
        self.pos = [x, y]
        self.dimensions = [w, h]
            
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

        screen.blit(self.image, (self.pos[0], self.pos[1]))
    
    def clicked(self, location, click):
        if click[0]:
            if (location[0] >= self.pos[0] and location[0] <= self.pos[0] + self.dimensions[0]) and (location[1] >= self.pos[1] and location[1] <= self.pos[1] + self.dimensions[1]):
                return True
