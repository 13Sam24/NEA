# Libraries being used
import pygame

slash = '\\'

# Things imported from other .py files I made
# from ui.Button import Button
from Screens.home import HomeScreen
from Screens.levels import LevelsScreen
from game import game

pygame.init()

screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Platformer')
WHITE = (255, 255, 255)
screen.fill(WHITE)
# Initialising the screens as objects
homeScreen = HomeScreen(screen, f'Assets{slash}HomeScreen{slash}Background.png', f'Assets{slash}HomeScreen{slash}Start.png', f'Assets{slash}HomeScreen{slash}OptionsButton.png', f'Assets{slash}HomeScreen{slash}Quit.png')
levelsScreen = LevelsScreen(screen, f'Assets{slash}LevelsScreen{slash}Background.png', f'Assets{slash}LevelsScreen{slash}Back.png', f'Assets{slash}LevelsScreen{slash}Level1.png', f'Assets{slash}LevelsScreen{slash}Level2.png', f'Assets{slash}LevelsScreen{slash}Level3.png', f'Assets{slash}LevelsScreen{slash}Level4.png')

# Setting the start screen to be the home screen
currentScreen = 'HomeScreen'

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Shows the home screen
	if currentScreen == 'HomeScreen':
		homeScreen.show()
		#pageSelect = homeScreen.buttonPress()

	
		match homeScreen.buttonPress():
			case 'LevelsScreen':
				currentScreen = 'LevelsScreen'
			case 'Options':
				currentScreen = 'Options'
			case 'Quit':
				running = False
		
	# Shows the levels screen
	if currentScreen == 'LevelsScreen':
		levelsScreen.show()
		pageSelect = levelsScreen.buttonPress()
		
		if pageSelect == 'HomeScreen':
			currentScreen = 'HomeScreen'
		if pageSelect == 'LevelOne':
			currentScreen = 'GameLevel1'
			game(screen, 'simple', 'null')
			keyPress = pygame.key.get_pressed()
			if keyPress[pygame.K_q]:
				print('k')
				ame(screen, 'simple', 'null')
			

	pygame.display.flip()

pygame.quit()