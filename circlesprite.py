import pygame

class circle_shape(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, radius):
        super().__init__(groups)  # Adds itself to given sprite groups
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        self.rect = self.image.get_rect(center=(x, y))
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)

    def update(self, dt):
        self.rect.x += self.velocity.x * dt
        self.rect.y += self.velocity.y * dt
