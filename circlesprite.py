import pygame

class CircleShape:
    def __init__(self, x, y, radius):
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        # Add a rect for collision detection
        self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)

    def update(self, dt):
        # Update rect position when the shape moves
        self.rect.centerx = self.position.x
        self.rect.centery = self.position.y
   
