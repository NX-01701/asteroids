import pygame
from constants import SHOT_RADIUS
from circle_shape import CircleShape
class Shot(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity):
        super().__init__()
        # Create a small surface for the bullet
        self.image = pygame.Surface((4, 4), pygame.SRCALPHA)
        pygame.draw.circle(self.image, 'white', (2, 2), 2)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        
        self.position = pygame.Vector2(x, y)
        self.velocity = velocity

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.center = self.position