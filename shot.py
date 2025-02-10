import pygame
from constants import SHOT_RADIUS
from circle_shape import CircleShape
class Shot(CircleShape):
    def __init__(self, position):
        super().__init__(position.x, position.y, SHOT_RADIUS)  
        self.velocity = pygame.Vector2(0, 0)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
        
    def update(self, delta_time):
        self.position += self.velocity * delta_time