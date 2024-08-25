import pygame
import sys
import random
import os

# Initialize Pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Asteroid Dodger")

asteroids = []
speed = 4
asteroid_speed = 2
spaceship = pygame.Rect(375, 500, 50, 50)

files = os.listdir('asteroids')
asteroid_images = [pygame.image.load(file) for file in files if file.endswith('.png')]

while True:
    # Increase speed over time
    asteroid_speed += 0.01
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if random.randint(1, 20) == 1:  # Controls the rate of spawning
        asteroid = pygame.Rect(random.randint(0, 750), 0, 50, 50)
        asteroids.append(asteroid)

        # Move asteroids
    for asteroid in asteroids[:]:
        asteroid.y += asteroid_speed
        if asteroid.y > 600:
            asteroids.remove(asteroid)

    pygame.draw.rect(screen, (0, 255, 0), spaceship)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and spaceship.left > 0:
        spaceship.x -= speed
    if keys[pygame.K_RIGHT] and spaceship.right < 800:
        spaceship.x += speed

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (0, 255, 0), spaceship)
    for asteroid in asteroids:
        pygame.draw.rect(screen, (255, 0, 0), asteroid)

    for asteroid in asteroids:
        if spaceship.colliderect(asteroid):
            pygame.quit()  # End the game if there's a collision
            sys.exit()

    pygame.display.flip()
    fps = 60
    clock = pygame.time.Clock()
    clock.tick(fps)