# Libraries being used
import pygame

slash = '\\'
#slash = '/'

# Things imported from other .py files I made
from Screens.home import HomeScreen
from Screens.levels import LevelsScreen
from game import Chunk
from Entities.Player.player import Player
from Entities.Player.movement import moveForwards, moveBackwards, playerjump
pygame.init()

# Makes and manages the screen in pygame
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Platformer')

FPS = pygame.time.Clock()
FPS.tick(60)

# Initialising the screens as objects
homeScreen = HomeScreen(screen, f'Assets{slash}HomeScreen{slash}Background.png', f'Assets{slash}HomeScreen{slash}Start.png', f'Assets{slash}HomeScreen{slash}OptionsButton.png', f'Assets{slash}HomeScreen{slash}Quit.png')
levelsScreen = LevelsScreen(screen, f'Assets{slash}LevelsScreen{slash}Background.png', f'Assets{slash}LevelsScreen{slash}Back.png', f'Assets{slash}LevelsScreen{slash}Level1.png', f'Assets{slash}LevelsScreen{slash}Level2.png', f'Assets{slash}LevelsScreen{slash}Level3.png', f'Assets{slash}LevelsScreen{slash}Level4.png')

# Setting the start screen to be the home screen
currentScreen = 'HomeScreen'
gameStart = True

# This is what keeps the game running
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Shows the home screen
	if currentScreen == 'HomeScreen':
		homeScreen.show()

		# Checks if button is pressed then goes to the correct page
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

		# Checks if a button is pressed and changes the currentScreen value as needed
		match levelsScreen.buttonPress():
			case 'HomeScreen':
				currentScreen = 'HomeScreen'
			case 'LevelOne':
				currentScreen = 'GameLevel1'

	if currentScreen == 'GameLevel1':
		
		while gameStart: # This means that It will only run this code once at the begining of the game
			Game = Chunk(screen, 1, 'null')
			Game.seedGenerate() # Generates the seed
			Game.start() # Makes the starting platform
			Game.makeChunk()
			Game.move(0)
			# Makes the player object and places it
			Player = Player(screen, 60, 960)

			gameStart = False # Stops this part of the code repeating

		# movement
		if Player.jumping:
			playerjump(Player, Game)
		keyPress = pygame.key.get_pressed() # Collects if a key is pressed
		if keyPress[pygame.K_d]: # forwards
			moveForwards(Player, Game)
		if keyPress[pygame.K_a]:
			moveBackwards(Player, Game)
		if keyPress[pygame.K_w] and Player.jumping == False:
			playerjump(Player, Game)

	pygame.display.flip()

pygame.quit()