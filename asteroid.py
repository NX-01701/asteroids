import pygame
import random
from constants import ASTEROID_MIN_RADIUS
from circle_shape import CircleShape
from constants import SCREEN_WIDTH, SCREEN_HEIGHT  # Don't forget to import these!

class Asteroid(pygame.sprite.Sprite):
    def __init__(self, x, y, size):
        super().__init__()
        # Create a surface with transparency
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        # Draw a white circle instead of filling the whole surface
        pygame.draw.circle(self.image, 'white', (size//2, size//2), size//2)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.radius = size//2
        
        # Initialize position and velocity (only once!)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)  
    
    def split(self):          # <-- This line starts the method
        self.kill()           # <-- Everything in the method should line up with this indent
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        
        # Calculate new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Create two new asteroids
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius * 4)  # multiply by 4 to get correct size
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius * 4)
        
        # Set their velocities (scaled up by 1.2)
        asteroid1.velocity = velocity1 * 1.2
        asteroid2.velocity = velocity2 * 1.2
        return asteroid1, asteroid2

    def update(self, dt):
        # Update position based on velocity
        self.position += self.velocity * dt
        
        # Screen wrapping
        self.position.x = self.position.x % SCREEN_WIDTH
        self.position.y = self.position.y % SCREEN_HEIGHT
        
        # Update rect position to match
        self.rect.center = self.position