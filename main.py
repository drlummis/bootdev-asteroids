# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Initialize pygame
    pygame.get_init()
    
    # Get a new GUI window
    screen = pygame.display.set_mode( (SCREEN_WIDTH, SCREEN_HEIGHT) )

    clock = pygame.time.Clock()
    dt = 0   # delta time

    # Create groups that will contain created objects.
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # When created an object will be added to each group in its containers.
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    # Create an asteroid field.
    asteroid_field = AsteroidField()

    # Create a player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    game_over = False
    while not game_over:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                    break
        if game_over:
            break

        # Fill screen with solid black
        screen.fill("black")

        # Draw all items that are in the group.
        for item in drawable:
            item.draw(screen)

        # Refresh the screen
        pygame.display.flip()
        
        # Pause for 1/60 of a second.
        # The .tick() method returns the amount in milliseconds since the
        # last time .tick() was called. Convert that value into seconds.
        dt = clock.tick(60) / 1000

        # Update all items that are in the group.
        for item in updatable:
            item.update(dt)

        # Check for collisions between asteroids and shots
        collision = False
        for item in asteroids:
            for shot in shots:
                collision = item.collision(shot)
                if collision:
                    item.kill()
                    shot.kill()
                    break
            if collision:
                break

        # Check for collisions between asteroids and player
        for item in asteroids:
            if item.collision(player):
                print("Game over!")
                game_over = True
                break

    pygame.quit()

if __name__ == "__main__":
    main()
