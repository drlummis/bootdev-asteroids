# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import Player
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

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    updatable.add(player)
    drawable.add(player)

    while True:
        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Fill screen with solid black
        screen.fill("black")

        # Draw the player
        for player in updatable:
            player.draw(screen)

        # Refresh the screen
        pygame.display.flip()
        
        # Pause for 1/60 of a second.
        # The .tick() method returns the amount in milliseconds since the
        # last time .tick() was called. Convert it into seconds.
        dt = clock.tick(60) / 1000

        # Update the player
        for player in drawable:
            player.update(dt)

if __name__ == "__main__":
    main()
