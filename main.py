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
asteroids = []  # Changed from pygame.sprite.Group()
shots = []

# Create initial asteroids
asteroid1 = Asteroid(100, 100, 50)  # Top left
asteroid1.velocity = pygame.Vector2(50, 20)
asteroids.append(asteroid1)  # Changed from asteroids.add()

asteroid2 = Asteroid(SCREEN_WIDTH - 100, 100, 50)  # Top right
asteroid2.velocity = pygame.Vector2(-50, 20)
asteroids.append(asteroid2)  # Changed from asteroids.add()

asteroid3 = Asteroid(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100, 50)  # Bottom middle
asteroid3.velocity = pygame.Vector2(20, -50)
asteroids.append(asteroid3)  # Changed from asteroids.add()

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
        if shot is not None:  # Only append if a shot was actually created
            shots.append(shot)
    
    # Update shots
    for shot in shots:
        shot.update(dt)
    
    # Update asteroids individually
    for asteroid in asteroids:
        asteroid.update(dt)
    
    # Remove this line since we're updating shots in the loop above
    # shots.update(dt)

    # Draw everything
    screen.fill("black")
    player.draw(screen)
    # Draw asteroids individually
    for asteroid in asteroids:
        asteroid.draw(screen)
    for shot in shots:
        shot.draw(screen)
    pygame.display.flip()

pygame.quit()