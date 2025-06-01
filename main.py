# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def Game_Loop():
	while True:
		for event in pygame.event.get():
    			if event.type == pygame.QUIT:
        			return
		screen.fill((0, 0, 0))
		pygame.display.flip()

def main():
	Game_Loop()
	pygame.init()
	print("Starting Asteroids!")
	print("Screen width:", SCREEN_WIDTH)
	print("Screen height:", SCREEN_HEIGHT)

if __name__ == "__main__":
	main()
