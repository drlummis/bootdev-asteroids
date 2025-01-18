import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        # Destroy the current asteroid
        self.kill()
        # If this was a small asteroid then don't split it.
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # New asteroids' directions will be at an angle to the current asteroid.
        angle = random.uniform(20, 50)
        vector1 = self.velocity.rotate(angle)
        vector2 = self.velocity.rotate(-angle)
        # Create 2 smaller asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        # New asteroids will be a bit faster
        asteroid1.velocity = vector1 * 1.2
        asteroid2.velocity = vector2 * 1.2
