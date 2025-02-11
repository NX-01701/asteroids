import pygame
import random
from circle_shape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(pygame.sprite.Sprite, CircleShape):
    def __init__(self, x, y, radius, velocity=None):
        pygame.sprite.Sprite.__init__(self, [])  # Initialize with empty group list
        CircleShape.__init__(self, x, y, radius)
        self.velocity = velocity or pygame.Vector2(0, 0)
        
        # Create a surface for the asteroid
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, "white", (radius, radius), radius, 2)
        self.rect = self.image.get_rect(center=self.position)

    def update(self, dt):
        super().update(dt)
        self.position += self.velocity * dt
        self.rect.center = self.position

    def split(self):
        self.kill()  # Remove this asteroid
        
        # If asteroid is too small, don't split it
        if self.radius <= ASTEROID_MIN_RADIUS:
            return []
            
        # Generate random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)
        
        # Create two new velocity vectors
        vel1 = self.velocity.rotate(random_angle)
        vel2 = self.velocity.rotate(-random_angle)
        
        # Calculate new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Create two new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius, vel1 * 1.2)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius, vel2 * 1.2)
        
        return [asteroid1, asteroid2]