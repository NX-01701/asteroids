import pygame
from player import Player
from asteroid import Asteroid
from shot import Shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create game objects
player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
asteroids = pygame.sprite.Group()  # Changed back to sprite group
shots = pygame.sprite.Group()      # Changed to sprite group

# Create initial asteroids
asteroid1 = Asteroid(100, 100, 50)  # Top left
asteroid1.velocity = pygame.Vector2(50, 20)
asteroids.add(asteroid1)  # Use add() for sprite groups

asteroid2 = Asteroid(SCREEN_WIDTH - 100, 100, 50)  # Top right
asteroid2.velocity = pygame.Vector2(-50, 20)
asteroids.add(asteroid2)  # Use add() for sprite groups

asteroid3 = Asteroid(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100, 50)  # Bottom middle
asteroid3.velocity = pygame.Vector2(20, -50)
asteroids.add(asteroid3)  # Use add() for sprite groups

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle timing
    dt = clock.tick(60) / 1000

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update game objects
    player.update(dt)
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        shot = player.shoot()
        if shot is not None:
            shots.add(shot)  # Use add() instead of append()

    # Update sprite groups
    asteroids.update(dt)
    shots.update(dt)

    # Check collisions
    for asteroid in asteroids:
        for shot in shots:
            if asteroid.rect.colliderect(shot.rect):
                print("Collision detected!")  # Debug print
                asteroid.kill()
                shot.kill()
    # Draw everything
    screen.fill("black")
    player.draw(screen)
    asteroids.draw(screen)
    shots.draw(screen)
    pygame.display.flip()
    

pygame.quit()