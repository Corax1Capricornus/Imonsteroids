from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = SHOT_RADIUS
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)


    def draw(self, screen):
       pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 1)


    def update(self, dt):
        self.position += self.velocity * dt