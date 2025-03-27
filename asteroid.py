import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.angle = 0
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            #Creating split asteroids
            self.angle = random.uniform(20, 50)
            self.velocity_1 = self.velocity.rotate(self.angle)
            self.velocity_2 = self.velocity.rotate(-self.angle)
            self.new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_1 = Asteroid(self.position.x, self.position.y, self.new_radius)
            asteroid_1.velocity = self.velocity_1 * 1.2
            asteroid_2 = Asteroid(self.position.x, self.position.y, self.new_radius)
            asteroid_2.velocity = self.velocity_2 * 1.2
