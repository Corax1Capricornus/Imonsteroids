from circleshape import *
import random
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x
        self.y = y
        self.radius = radius


    def draw(self, screen):
       pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt


    def split(self):
        # Split the asteroid into two smaller ones
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            self.kill()
            random_angle = random.uniform(20, 50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid1.velocity = self.velocity.rotate(random_angle)*1.2
            asteroid2.velocity = self.velocity.rotate(-random_angle)*1.2