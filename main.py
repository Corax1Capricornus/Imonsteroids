# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
        pygame.init()
        clock = pygame.time.Clock()
        dt = clock.tick(60) / 1000   
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        Player.containers = (updatable, drawable)
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        asteroids = pygame.sprite.Group()
        Asteroid.containers = (asteroids, updatable, drawable)
        AsteroidField.containers = (updatable)
        asteroid_field = AsteroidField()
        shots = pygame.sprite.Group()
        Shot.containers = (shots, updatable, drawable)       
        
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                return
                        elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                        player.shoot()
                screen.fill((0, 0, 0))
                dt = clock.tick(60) / 1000
                updatable.update(dt)          
                for asteroid in asteroids:
                        if asteroid.collision(player):
                                print("Game Over!")
                                pygame.quit()
                                return
                for shot in shots:
                        for asteroid in asteroids:
                                if shot.collision(asteroid):
                                        shot.kill()
                                        asteroid.kill()
                for thing in drawable:
                        thing.draw(screen)
                pygame.display.flip()
        print("Starting Asteroids!")
        print("Screen width:", SCREEN_WIDTH)
        print("Screen height:", SCREEN_HEIGHT)
        
        

if __name__ == "__main__":
        main()
